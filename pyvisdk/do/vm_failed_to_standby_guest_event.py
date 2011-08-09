
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFailedToStandbyGuestEvent(VmEvent):
    '''This event records a failure to set the guest on a virtual machine to a standby
        state.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VmFailedToStandbyGuestEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

