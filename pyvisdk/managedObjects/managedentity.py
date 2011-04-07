'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk import consts
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.core import ManagedObjectReference
from pyvisdk.managedObjects import ManagedEntities
import logging
import types

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class TaskDelegate(object):
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
            log.debug("Waiting for task to Complete")
            self.core.waitForTask(rv)
        return rv
   
class ManagedEntity(object):
    __slots__ = ['props']
    def __init__(self, core, methods=[], props=[], name=None, ref=None):
        self.ref = ref
        self.core = core
        self.client = core.client
        self.service = core.client.service
        if name:
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
                    self.__dict__[name] = self._clean(value)
            except AttributeError, e:
                log.warning("[WARNING] [%s] %s" %  (name, e))
                
    def _clean(self, objectContent):
        if type(objectContent) == types.ListType:
            out = []
            for x in objectContent:
                out.append(self._clean(x))
            return out
        elif objectContent.__class__.__name__ == "ObjectContent":
            obj = objectContent.obj
            if obj._type in consts.ManagedEntityTypes:
                return ManagedEntities[obj._type](self, objectContent)
        elif objectContent.__class__.__name__ == "ManagedObjectReference" and objectContent._type in ManagedEntityTypes:
            return ManagedEntities[objectContent._type](self.core, objectContent)
        else:
            log.debug("Unable to clean: %s" % objectContent)
        return objectContent
    
    def __getattr__(self, _name):
        if _name in self.props:
            self.update(_name)
        try:
            return object.__getattribute__(self, _name)
        except AttributeError, e:
            # try it with _Task on the end...
            return object.__getattribute__(self, _name + "_Task")
            











