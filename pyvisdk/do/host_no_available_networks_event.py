
from pyvisdk.do.host_das_event import HostDasEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNoAvailableNetworksEvent(HostDasEvent):
    '''This event records the fact that a host does not have any available networks for
        HA communication
    '''
    
    def __init__(self, ips):
        # MUST define these
        super(HostNoAvailableNetworksEvent, self).__init__()
    
        self.data['ips'] = ips
    
    
    @property
    def ips(self):
        '''The comma-separated list of used networks
        '''
        return self.data['ips']

