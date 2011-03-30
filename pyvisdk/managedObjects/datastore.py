'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.managedObjects.managedentity import ManagedEntity
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class Datastore(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        # MUST define these
        self.type = ManagedEntityTypes.Datastore
        
        props = [ "browser", "info", "summary", "capability", "vm"]
        
        methods = ["DestroyDatastore", "RefreshDatastore", "RefreshDatastoreStorageInfo", "RenameDatastore",
                             "UpdateVirtualMachineFiles_Task"]
        
        super(Datastore, self).__init__(core, methods, props, name, ref)
        
