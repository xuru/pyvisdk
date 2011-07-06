'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.managedObjects.managedentity import ManagedEntity
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class ResourcePool(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        # MUST define these first
        # -- start --
        self.type = ManagedEntityTypes.ResourcePool
        
        # properties for this managed object
        props = [ "config", "owner", "runtime", "summary"]
        
        # methods for this managed object
        methods = ["CreateChildVM_Task", "CreateResourcePool", "CreateVApp", \
                   "DestroyChildren", "ImportVApp", "MoveIntoResourcePool", \
                   "QueryResourceConfigOption", "RefreshRuntime", "RegisterChildVM_Task", \
                   "UpdateChildResourceConfiguration", "UpdateConfig"]
        # -- end --
        
        super(ResourcePool, self).__init__(core, methods, props, name, ref)
        
