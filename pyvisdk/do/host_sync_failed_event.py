
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSyncFailedEvent(HostEvent):
    '''This event records a failure to sync up with the VirtualCenter agent on the host
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(HostSyncFailedEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

