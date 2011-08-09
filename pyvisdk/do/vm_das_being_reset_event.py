
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDasBeingResetEvent(VmEvent):
    '''This event records when a virtual machine is reset by HA VM Health Monitoring on
        hosts that do not support the create screenshot api or if the
        createscreenshot api fails.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VmDasBeingResetEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason why this vm is being reset
        '''
        return self.data['reason']

