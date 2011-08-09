
from pyvisdk.do.host_das_event import HostDasEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMissingNetworksEvent(HostDasEvent):
    '''This event records the fact that a host is missing networks that other hosts are
        using for HA communication
    '''
    
    def __init__(self, ips):
        # MUST define these
        super(HostMissingNetworksEvent, self).__init__()
    
        self.data['ips'] = ips
    
    
    @property
    def ips(self):
        '''
        '''
        return self.data['ips']

