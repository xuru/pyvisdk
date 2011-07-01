'''
Created on Mar 8, 2011

@author: eplaster
'''

from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.managedObjects.managedentity import ManagedEntity
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class VirtualMachineSnapshot(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        """ 
        VirtualMachineSnapshot
        """
        # MUST define these
        self.type = ManagedEntityTypes.VirtualMachineSnapshot
        
        props = [ "childSnapshot", "config" ]
        
        methods = ["RemoveSnapshot_Task", "RenameSnapshot", "RevertToSnapshot_Task"]
        
        # we don't have the normal default props, so don't try it in the base class
        super(VirtualMachineSnapshot, self).__init__(core, methods, props, name, ref, skip_default_props=True)

        if ref:
            self.name = ref.value