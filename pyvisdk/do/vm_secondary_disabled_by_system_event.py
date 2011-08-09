
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmSecondaryDisabledBySystemEvent(VmEvent):
    '''This event records that a fault tolerance secondary VM has been disabled by
        vCenter because the VM could not be powered on.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VmSecondaryDisabledBySystemEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''
        '''
        return self.data['reason']

