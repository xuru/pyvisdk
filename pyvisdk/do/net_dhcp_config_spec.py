
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetDhcpConfigSpec(DynamicData):
    '''Dynamic Host Configuration Protocol Configuration for IP version 4 and version 6.
    '''
    
    def __init__(self, ipv4, ipv6):
        # MUST define these
        super(NetDhcpConfigSpec, self).__init__()
    
        self.data['ipv4'] = ipv4
        self.data['ipv6'] = ipv6
    
    
    @property
    def ipv4(self):
        '''Configure IPv4 DHCP client settings.
        '''
        return self.data['ipv4']

    @property
    def ipv6(self):
        '''Configure IPv6 DHCP client settings.
        '''
        return self.data['ipv6']

