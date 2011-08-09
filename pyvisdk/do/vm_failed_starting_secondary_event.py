
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFailedStartingSecondaryEvent(VmEvent):
    '''This event records vmotion failure when starting a secondary VM.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VmFailedStartingSecondaryEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason for the failure. See VmFailedStartingSecondaryEventFailureReason
        '''
        return self.data['reason']

