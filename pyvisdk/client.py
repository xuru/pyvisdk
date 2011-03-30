'''
Created on Mar 6, 2011

@author: eplaster
'''
from pyvisdk import consts
from pyvisdk.managedObjects import ManagedEntities
from suds import MethodNotFound
import logging
import os.path
import suds
import types

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class Delegate:
    """ delegates to the real method, and cleans up the return value """
    
    def __init__(self, method):
        """ Initializes the delagate with the method to proxy """
        self.__target = method
        
    def __call__(self, *args, **kwargs):
        """ calls original method """
        log.debug("Calling %s" % self.__target.method.name)
        rv = self.clean(self.__target(*args, **kwargs))
        #self.dump(rv)
        return rv

    def clean(self, objectContent):
        if type(objectContent) == types.ListType:
            out = []
            for x in objectContent:
                out.append(self.clean(x))
            return out
        elif objectContent.__class__.__name__ == "ObjectContent":
            obj = objectContent.obj
            print obj._type
            if obj._type in consts.ManagedEntityTypes:
                print obj._type
                return ManagedEntities[obj._type](self, objectContent)
        return objectContent
            
    def dump(self, rv):
        print "Classname: " + rv.__class__.__name__
        if rv.__class__.__name__ == "ServiceContent":
            return
        
        if type(rv) == types.ListType:
            for x in rv:
                self.dump(x)
        
        if rv.__class__.__name__ == "ObjectContent":
            print "="*80
            print rv
            print
                
        
## end of http://code.activestate.com/recipes/496860/ }}}

class Client(object):
    '''
    The Client class acts as a proxy to the suds.client.Client class, in that it fixes the
    ManagedObjectReference objects and provides a more streamline interface specific to VISDK
    '''
    def __init__(self, server):
        '''
        Constructor
        '''
        wsdl_dir = os.path.abspath(os.path.dirname(__file__))
        url = "https://" + server + '/sdk'
        client = suds.client.Client("file://" + os.path.join(wsdl_dir, 'wsdl', 'vimService.wsdl'))
        client.set_options(faults=True)
        client.set_options(location=url)
        self.service = client.service
        self.url = url
        self.client = client
        self.server = server

    #
    # proxying (special cases)
    #
    def __getattribute__(self, attr):
        service = super(Client, self).__getattribute__("service")
        
        # try the service
        try:
            _attr = getattr(service, attr)
            if _attr.__class__ == suds.client.Method:
                return Delegate(_attr)
            else:
                return _attr
        except (AttributeError, MethodNotFound):
            # see if it's in the client object
            try:
                client = super(Client, self).__getattribute__("client")
                _attr = getattr(client, attr)
                return _attr
            except (AttributeError, MethodNotFound):
                # if it's a member of this class...
                return super(Client, self).__getattribute__(attr)
            
    
    def typeIsA(self, searchType, foundType):
        if searchType == foundType:
            return True
        elif searchType == "ManagedEntity":
            for me in consts.ManagedEntityTypes:
                if me == foundType:
                    return True
        elif searchType == "ComputeResource":
            for me in consts.ComputeResourcesTypes:
                if me == foundType:
                    return True
        elif searchType == "HistoryCollector":
            for me in consts.HistoryCollectorTypes:
                if me == foundType:
                    return True
        return False

    #def __delattr__(self, name):
    #    delattr(object.__getattribute__(self, "service"), name)
        
    #def __setattr__(self, name, value):
    #    setattr(object.__getattribute__(self, "service"), name, value)
    
    #def __nonzero__(self):
    #    return bool(object.__getattribute__(self, "service"))
    
    #def __str__(self):
    #    return str(object.__getattribute__(self, "service"))
    
    #def __repr__(self):
    #    return repr(object.__getattribute__(self, "service"))