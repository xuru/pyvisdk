
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpConfigInfo(DynamicData):
    '''Protocol version independent address reporting data object for network interfaces.
    '''
    
    def __init__(self, autoConfigurationEnabled, dhcp, ipAddress):
        # MUST define these
        super(NetIpConfigInfo, self).__init__()
    
        self.data['autoConfigurationEnabled'] = autoConfigurationEnabled
        self.data['dhcp'] = dhcp
        self.data['ipAddress'] = ipAddress
    
    
    @property
    def autoConfigurationEnabled(self):
        '''Enable or disable ICMPv6 router solictitation requests from a given interface to
        acquire an IPv6 address and default gateway route from zero, one or more
        routers on the connected network. If not set then ICMPv6 is not available
        on this system, See vim.host.Network.Capabilities
        '''
        return self.data['autoConfigurationEnabled']

    @property
    def dhcp(self):
        '''Client side DHCP for a given interface.
        '''
        return self.data['dhcp']

    @property
    def ipAddress(self):
        '''Zero, one or more manual (static) assigned IP addresses to be configured on a
        given interface.
        '''
        return self.data['ipAddress']

