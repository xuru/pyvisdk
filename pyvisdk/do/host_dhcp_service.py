
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDhcpService(DynamicData):
    '''A dynamic host control protocol (DHCP) service instance serves IP addresses to a
        single virtual network subnet. The instances may be handled collectively
        by a single server. This decision can be made during implementation.
    '''
    
    def __init__(self, key, spec):
        # MUST define these
        super(HostDhcpService, self).__init__()
    
        self.data['key'] = key
        self.data['spec'] = spec
    
    
    @property
    def key(self):
        '''The instance ID of the DHCP service.
        '''
        return self.data['key']

    @property
    def spec(self):
        '''Configurable properties for the DHCP service.
        '''
        return self.data['spec']

