
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostShutdownEvent(HostEvent):
    '''This event records the shutdown of a host.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(HostShutdownEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason for the host shutdown.
        '''
        return self.data['reason']

