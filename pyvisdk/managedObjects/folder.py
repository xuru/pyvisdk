'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.managedObjects.managedentity import ManagedEntity
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class Folder(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        # MUST define these
        self.type = ManagedEntityTypes.Folder
        props = [ "childEntity", "childType"]
        
        methods = ["AddStandaloneHost_Task", "CreateCluster", "CreateClusterEx", 
                    "CreateDatacenter", "CreateDVS_Task", "CreateFolder", "CreateVM_Task", 
                    "MoveIntoFolder_Task", "RegisterVM_Task", "UnregisterAndDestroy_Task"]
        
        super(Folder, self).__init__(core, methods, props, name, ref)
        
