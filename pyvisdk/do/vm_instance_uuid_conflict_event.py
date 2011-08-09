
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmInstanceUuidConflictEvent(VmEvent):
    '''This event records a conflict of virtual machine instance UUIDs.
    '''
    
    def __init__(self, conflictedVm, instanceUuid):
        # MUST define these
        super(VmInstanceUuidConflictEvent, self).__init__()
    
        self.data['conflictedVm'] = conflictedVm
        self.data['instanceUuid'] = instanceUuid
    
    
    @property
    def conflictedVm(self):
        '''The virtual machine whose instance UUID conflicts with the current virtual
        machine's instance UUID.
        '''
        return self.data['conflictedVm']

    @property
    def instanceUuid(self):
        '''The instance UUID in conflict.
        '''
        return self.data['instanceUuid']

