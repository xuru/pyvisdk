
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaIPCapabilities(DynamicData):
    '''The IP Capabilities for the host bus adapter
    '''
    
    def __init__(self, addressSettable, alternateDnsServerAddressSettable, arpRedirectSettable, defaultGatewaySettable, hostNameAsTargetAddress, ipConfigurationMethodSettable, ipv6Supported, mtuSettable, nameAliasSettable, primaryDnsServerAddressSettable, subnetMaskSettable):
        # MUST define these
        super(HostInternetScsiHbaIPCapabilities, self).__init__()
    
        self.data['addressSettable'] = addressSettable
        self.data['alternateDnsServerAddressSettable'] = alternateDnsServerAddressSettable
        self.data['arpRedirectSettable'] = arpRedirectSettable
        self.data['defaultGatewaySettable'] = defaultGatewaySettable
        self.data['hostNameAsTargetAddress'] = hostNameAsTargetAddress
        self.data['ipConfigurationMethodSettable'] = ipConfigurationMethodSettable
        self.data['ipv6Supported'] = ipv6Supported
        self.data['mtuSettable'] = mtuSettable
        self.data['nameAliasSettable'] = nameAliasSettable
        self.data['primaryDnsServerAddressSettable'] = primaryDnsServerAddressSettable
        self.data['subnetMaskSettable'] = subnetMaskSettable
    
    
    @property
    def addressSettable(self):
        '''True if the host bus adapter supports setting its IP address.
        '''
        return self.data['addressSettable']

    @property
    def alternateDnsServerAddressSettable(self):
        '''True if the host bus adapter supports setting its secondary DNS.
        '''
        return self.data['alternateDnsServerAddressSettable']

    @property
    def arpRedirectSettable(self):
        '''True if the host bus adapter supports setting its ARP Redirect value
        '''
        return self.data['arpRedirectSettable']

    @property
    def defaultGatewaySettable(self):
        '''True if the host bus adapter supports setting its gateway.
        '''
        return self.data['defaultGatewaySettable']

    @property
    def hostNameAsTargetAddress(self):
        '''True if the discovery and static targets can be configured with a host name as
        opposed to an IP address.
        '''
        return self.data['hostNameAsTargetAddress']

    @property
    def ipConfigurationMethodSettable(self):
        '''True if the host bus adapter supports DHCP.
        '''
        return self.data['ipConfigurationMethodSettable']

    @property
    def ipv6Supported(self):
        '''True if the host bus adapter supports the use of IPv6 addresses
        '''
        return self.data['ipv6Supported']

    @property
    def mtuSettable(self):
        '''True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc)
        '''
        return self.data['mtuSettable']

    @property
    def nameAliasSettable(self):
        '''True if the host bus adapter supports setting its name and alias
        '''
        return self.data['nameAliasSettable']

    @property
    def primaryDnsServerAddressSettable(self):
        '''True if the host bus adapter supports setting its primary DNS.
        '''
        return self.data['primaryDnsServerAddressSettable']

    @property
    def subnetMaskSettable(self):
        '''True if the host bus adapter supports setting its subnet mask.
        '''
        return self.data['subnetMaskSettable']

