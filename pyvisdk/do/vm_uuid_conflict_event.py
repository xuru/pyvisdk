
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmUuidConflictEvent(VmEvent):
    '''This event records a conflict of virtual machine BIOS UUIDs.
    '''
    
    def __init__(self, conflictedVm, uuid):
        # MUST define these
        super(VmUuidConflictEvent, self).__init__()
    
        self.data['conflictedVm'] = conflictedVm
        self.data['uuid'] = uuid
    
    
    @property
    def conflictedVm(self):
        '''The virtual machine whose UUID conflicts with the current virtual machine's UUID.
        '''
        return self.data['conflictedVm']

    @property
    def uuid(self):
        '''The BIOS UUID in conflict.
        '''
        return self.data['uuid']

