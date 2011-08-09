
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFailedToResetEvent(VmEvent):
    '''This event records a failure to reset a virtual machine.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VmFailedToResetEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

