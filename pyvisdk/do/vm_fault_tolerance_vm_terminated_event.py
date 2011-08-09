
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFaultToleranceVmTerminatedEvent(VmEvent):
    '''This event records a secondary or primary VM is terminated. The reason could be :
        divergence, lost connection to secondary, partial hardware failure of
        secondary, or by user.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VmFaultToleranceVmTerminatedEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''
        '''
        return self.data['reason']

