
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpInconsistentEvent(HostEvent):
    '''This event records that the IP address resolution returned different addresses on
        the host. Please check your host's network configuration.
    '''
    
    def __init__(self, ipAddress, ipAddress2):
        # MUST define these
        super(HostIpInconsistentEvent, self).__init__()
    
        self.data['ipAddress'] = ipAddress
        self.data['ipAddress2'] = ipAddress2
    
    
    @property
    def ipAddress(self):
        '''
        '''
        return self.data['ipAddress']

    @property
    def ipAddress2(self):
        '''
        '''
        return self.data['ipAddress2']

