'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.core import ManagedObjectReference
import logging
import time
import types

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class TaskDelegate:
    """ delegates to the real method, and waits for the task to complete"""
    
    def __init__(self, cls, name):
        """ Initializes the delagate with the method to proxy """
        self.__target = getattr(cls.service, name)
        self.ref = cls.ref
        self.name = name
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
            print "Waiting for task to Complete"
            self.core.waitForTask(rv)
        return rv
    
class ManagedEntity(object):
    def __init__(self, core, methods=[], props=[], name=None, ref=None):
        self.ref = ref
        self.core = core
        self.client = core.client
        self.service = core.client.service
        self.name = name
        self.props = ["configIssue", "configStatus", "name", "parent"] + props
        
        if not getattr(self, 'type'):
            self.type = ManagedEntityTypes.ManagedEntity
            
        if ref:
            self.ref = ManagedObjectReference(self.type, ref.value)
            
        if not methods:
            methods = ["Destroy_Task", "Reload, Rename_Task"]
            
        for method in methods:
            try:
                self.__dict__[method] = TaskDelegate(self, method)
            except Exception, e:
                log.error("%s" % e)
        
    def update(self, prop):
        if type(prop) == types.ListType:
            for x in prop:
                self.update(x)
        
        data = self.core.getDynamicProperty(self.ref, prop)
        for name, value in data.items():
            try:
                if name in self.props:
                    log.debug("[%s] %s" % (name, value.__class__.__name__))
                    self.__dict__[name] = value
            except AttributeError, e:
                log.warning("[WARNING] [%s] %s" %  (name, e))
                
    
    def __getattribute__( self, _name ):
        """
        Return a proxy wrapper object if this is a method call.
        """
        try:
            return object.__getattribute__(self, _name)
        except AttributeError:
            try:
                return object.__getattribute__(self, _name+"_Task")
            except AttributeError:
                if _name in self.props:
                    self.update(_name)
                    time.sleep(1)
                    return object.__getattribute__(self, _name)
                else:
                    raise

