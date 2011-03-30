'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.managedObjects.managedentity import ManagedEntity
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class ComputeResource(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        # MUST define these first
        # -- start --
        self.type = ManagedEntityTypes.ComputeResource
        
        # properties for this managed object
        props = [ "configurationEx", "datastore", "environmentBrowser", "host", 
                 "network", "resourcePool", 'summary']
        
        # methods for this managed object
        methods = ["ReconfigureComputeResource_Task"]
        # -- end --
        
        super(ComputeResource, self).__init__(core, methods, props, name, ref)
        
