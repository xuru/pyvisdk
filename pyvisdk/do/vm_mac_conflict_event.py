
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmMacConflictEvent(VmEvent):
    '''This event records a MAC address conflict for a virtual machine.
    '''
    
    def __init__(self, conflictedVm, mac):
        # MUST define these
        super(VmMacConflictEvent, self).__init__()
    
        self.data['conflictedVm'] = conflictedVm
        self.data['mac'] = mac
    
    
    @property
    def conflictedVm(self):
        '''The virtual machine whose MAC address conflicts with the current virtual machine's
        address.
        '''
        return self.data['conflictedVm']

    @property
    def mac(self):
        '''The MAC address that is in conflict.
        '''
        return self.data['mac']

