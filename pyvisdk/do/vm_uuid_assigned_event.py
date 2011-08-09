
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmUuidAssignedEvent(VmEvent):
    '''This event records the assignment of a new BIOS UUID to a virtual machine.
    '''
    
    def __init__(self, uuid):
        # MUST define these
        super(VmUuidAssignedEvent, self).__init__()
    
        self.data['uuid'] = uuid
    
    
    @property
    def uuid(self):
        '''The new BIOS UUID.
        '''
        return self.data['uuid']

