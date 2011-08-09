
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFailedRelayoutEvent(VmEvent):
    '''This event records a specific failure to relay out a virtual machine, such as a
        failure to access the disk.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VmFailedRelayoutEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''
        '''
        return self.data['reason']

