
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpConfigSpec(DynamicData):
    '''Internet Protocol Address Configuration for version 4 and version 6.
    '''
    
    def __init__(self, autoConfigurationEnabled, dhcp, ipAddress):
        # MUST define these
        super(NetIpConfigSpec, self).__init__()
    
        self.data['autoConfigurationEnabled'] = autoConfigurationEnabled
        self.data['dhcp'] = dhcp
        self.data['ipAddress'] = ipAddress
    
    
    @property
    def autoConfigurationEnabled(self):
        '''Enable or disable ICMPv6 router solictitation requests from a given interface to
        acquire an IPv6 address and default gateway route from zero, one or more
        routers on the connected network.
        '''
        return self.data['autoConfigurationEnabled']

    @property
    def dhcp(self):
        '''Configure client side DHCP for a given interface.
        '''
        return self.data['dhcp']

    @property
    def ipAddress(self):
        '''A set of manual (static) IP addresses to be configured on a given interface.
        '''
        return self.data['ipAddress']

