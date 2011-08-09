
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetDhcpConfigInfo(DynamicData):
    '''Dynamic Host Configuration Protocol reporting for IP version 4 and version 6.
    '''
    
    def __init__(self, ipv4, ipv6):
        # MUST define these
        super(NetDhcpConfigInfo, self).__init__()
    
        self.data['ipv4'] = ipv4
        self.data['ipv6'] = ipv6
    
    
    @property
    def ipv4(self):
        '''IPv4 DHCP client settings.
        '''
        return self.data['ipv4']

    @property
    def ipv6(self):
        '''IPv6 DHCP client settings.
        '''
        return self.data['ipv6']

