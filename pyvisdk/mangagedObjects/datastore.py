'''
Created on Mar 8, 2011

@author: eplaster
'''
from mangagedObjects.managedentity import ManagedEntity
from pyvisdk import consts
from pyvisdk.consts import ManagedObjectReference
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class Datastore(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        # MUST define these
        props = [ "browser", "info", "summary", "capability"]
        super(Datastore, self).__init__(core, props, name, ref)
        
        self.type = consts.Datastore # type used to get to the virtual disks
        
        self.name = name
        self.ref = ref
        if ref:
            self.ref = ManagedObjectReference(consts.Datastore, ref.value)
        self.parse()
        
    def update(self, prop):
        super(Datastore, self).update(prop)
        
        log.debug("*********** %s update **************" % self.__class__.__name__)
        for name, value in prop.items():
            if name == 'info':
                log.debug("[%s] %s" % (name, value.__class__.__name__))
                # VmfsDatastoreInfo
                self.info = value
            
            elif name == 'summary':
                log.debug("[%s] %s" % (name, value.__class__.__name__))
                self.summary = value
            
            elif name == 'capability':
                log.debug("[%s] %s" % (name, value.__class__.__name__))
                self.capability = value
            
            elif name == 'browser':
                log.debug("[%s] %s" % (name, value.__class__.__name__))
                self.browser = value
            
    def parse(self):
        info = self.core.getDynamicProperty(self.ref, self.props)
        self.update(info)
        
    def __str__(self):
        return "<%s> %s" % (self.type, self.name)
