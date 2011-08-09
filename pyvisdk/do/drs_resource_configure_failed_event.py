
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DrsResourceConfigureFailedEvent(HostEvent):
    '''This event records when resource configuration specification synchronization fails
        on a host.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(DrsResourceConfigureFailedEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

