
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDisconnectedEvent(HostEvent):
    '''This event records a disconnection from a host.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(HostDisconnectedEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''Reason why the host was disconnected.
        '''
        return self.data['reason']

