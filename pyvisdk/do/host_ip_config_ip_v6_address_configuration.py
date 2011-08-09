
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpConfigIpV6AddressConfiguration(DynamicData):
    '''The ipv6 address configuration
    '''
    
    def __init__(self, autoConfigurationEnabled, dhcpV6Enabled, ipV6Address):
        # MUST define these
        super(HostIpConfigIpV6AddressConfiguration, self).__init__()
    
        self.data['autoConfigurationEnabled'] = autoConfigurationEnabled
        self.data['dhcpV6Enabled'] = dhcpV6Enabled
        self.data['ipV6Address'] = ipV6Address
    
    
    @property
    def autoConfigurationEnabled(self):
        '''Specify if IPv6 address and routing information information be enabled or not as
        per RFC 2462.
        '''
        return self.data['autoConfigurationEnabled']

    @property
    def dhcpV6Enabled(self):
        '''The flag to indicate whether or not DHCP (dynamic host control protocol) is
        enabled to obtain an ipV6 address. If this property is set to true, an
        ipV6 address is configured through dhcpV6.
        '''
        return self.data['dhcpV6Enabled']

    @property
    def ipV6Address(self):
        '''Ipv6 adrresses configured on the interface. The global addresses can be configured
        through DHCP, stateless or manual configuration. Link local addresses can
        be only configured with the origin set to other.
        '''
        return self.data['ipV6Address']

