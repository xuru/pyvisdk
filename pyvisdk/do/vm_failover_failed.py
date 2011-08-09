
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFailoverFailed(VmEvent):
    '''This event records when a virtual machine failover was unsuccessful.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VmFailoverFailed, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason for the failure
        '''
        return self.data['reason']

