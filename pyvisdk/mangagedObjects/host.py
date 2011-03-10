'''
Created on Mar 8, 2011

@author: eplaster
'''
from mangagedObjects.datastore import Datastore
from mangagedObjects.managedentity import ManagedEntity
from pyvisdk import consts
from pyvisdk.consts import ManagedObjectReference
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class HostSystem(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
            # MUST define these
        props = [ "name", "datastore"]
        super(HostSystem, self).__init__(core, props, name, ref)
        
        self.datastores = {}
        self.type = consts.HostSystem
        self.name = name
        if ref:
            self.ref = ManagedObjectReference(consts.HostSystem, ref.value)
        self.parse()
    
    def update(self, prop):
        super(HostSystem, self).update(prop)
        
        log.debug("*********** %s update **************" % self.__class__.__name__)
        for name, value in prop.items():
            if name == 'datastore':
                for dsmor in value:
                    ds = Datastore(self.core, ref=dsmor)
                    self.datastores[ds.name] = ds
        
    def parse(self):
        for prop in self.props:
            info = self.core.getDynamicProperty(self.ref, prop)
            self.update(info)
    
    def __str__(self):
        return "<%s> %s" % (self.type, self.name)
