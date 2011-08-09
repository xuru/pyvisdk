'''
Created on Mar 8, 2011

@author: eplaster
'''
import suds, suds.sax, logging, types
from dataflake.cache.timeout import TimeoutCache

from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.exceptions import PyVisdkError
import pyvisdk.mo
import pyvisdk.do

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def MOFactory(core, ref):
    log.debug("REF: %s" % ref)
    
    # if we have an obj, then obj is the managed object reference
    if hasattr(ref, 'obj'):
        _class = eval("pyvisdk.mo.%s" % ref.obj._type)
        return _class(core,  name=ref.propSet[0].val, ref=ref.obj)
    
    # check if ref is the managed object reference
    elif (hasattr(ref, '_type') and hasattr(ref, 'value')) or ref.__class__.__name__ == 'ManagedObjectReference':
        _class = eval("pyvisdk.mo.%s" % ref._type)
        return _class(core,  ref=ref)
    
    # make sure we catch anything else...
    else:
        raise PyVisdkError("Unknown managed object reference: %s" % ref)

class ManagedObjectReference(suds.sudsobject.Property):
    """Custom class to replace the suds generated class, which lacks _type."""
    def __init__(self, _type, value):
        suds.sudsobject.Property.__init__(self, value)
        self._type = _type
        


class TaskDelegate(object):
    """ delegates to the real method, and waits for the task to complete"""
    
    def __init__(self, cls, name):
        """ Initializes the delagate with the method to proxy """
        self.__target = getattr(cls.service, name)
        self.name = name
        self.ref = cls.ref
        self.core = cls.core
        
    def __call__(self, *args, **kwargs):
        """ calls original method """
        log.debug("Calling %s" % self.__target.method.name)
        if len(args):
            args = list(args)
            args.insert(0, self.ref)
        else:
            args = (self.ref, )
        rv = self.__target(*args, **kwargs)
        if self.name[-5:] == '_Task':
            log.debug("Waiting for task to Complete")
            self.core.waitForTask(rv)
        return rv

    def _return_value(self, rv):
        if isinstance(rv, list):
            return [self._return_value(x) for x in rv]
        if 'suds.sudsobject' in str(rv.__class__):
            new_obj = eval("pyvisdk.do.%s()" % rv.__class__.__name__)
            for attr in dir(rv):
                if attr[0] != '_':
                    if isinstance(attr, suds.sax.text.Text):
                        new_obj.data[str(attr)] = str(eval('rv.%s' % attr))
                    elif 'suds.sudsobject' in str(eval('rv.%s' % attr)):
                        new_obj.data[str(attr)] = self._return_value(eval('rv.%s' % attr))
                    else:
                        new_obj.data[str(attr)] = eval("rv.%s" % attr)
            return new_obj
        else:
            return rv
                    
   
class BaseEntity(object):
    def __init__(self, core, name=None, ref=None, type=None):
        self.core = core
        self.name = name
        self.ref = ref
        self.type = type
        
        self.cache = TimeoutCache()
        self.cache.setTimeout(60) # timeout to one minute
        
        self.client = core.client
        self.service = core.client.service
        
        if self.ref:
            self.ref = ManagedObjectReference(self.type, self.ref.value)
    
            # we have a ref, AND we don't already have a name, we can get the name from it...
            if not self.name:
                self.name = self.ref.value
            
    def update(self, prop):
        if type(prop) == types.ListType:
            for x in prop:
                self.update(x)
                
        data = self.cache.get(prop, default=None)
        if not data:
            data = self.core.getObjectProperties(self.ref, prop)
            self.cache.set(prop, data)
            
        return data
                

    def delegate(self, name):
        log.debug("Delegating %s" % name)
        return TaskDelegate(self, name)











