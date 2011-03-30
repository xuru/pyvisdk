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
    def __init__(self, vm, name=None, ref=None):
        """ 
        VirtualMachineSnapshot
        """
        # MUST define these
        self.type = ManagedEntityTypes.VirtualMachineSnapshot
        self.vm = vm
        
        props = [ "childSnapshot", "config" ]
        
        methods = ["RemoveSnapshot_Task", "RenameSnapshot", "RevertToSnapshot_Task"]
        
        super(VirtualMachineSnapshot, self).__init__(vm.core, methods, props, name, ref)
