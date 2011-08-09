
from pyvisdk.do.host_das_event import HostDasEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostExtraNetworksEvent(HostDasEvent):
    '''This event records the fact that a host has extra networks not used by other hosts
        for HA communication
    '''
    
    def __init__(self, ips):
        # MUST define these
        super(HostExtraNetworksEvent, self).__init__()
    
        self.data['ips'] = ips
    
    
    @property
    def ips(self):
        '''The comma-separated list of extra networks
        '''
        return self.data['ips']

