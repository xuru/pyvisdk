
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaIPProperties(DynamicData):
    '''The IP properties for the host bus adapter
    '''
    
    def __init__(self, address, alternateDnsServerAddress, arpRedirectEnabled, defaultGateway, dhcpConfigurationEnabled, ipv6Address, ipv6DefaultGateway, ipv6SubnetMask, jumboFramesEnabled, mac, mtu, primaryDnsServerAddress, subnetMask):
        # MUST define these
        super(HostInternetScsiHbaIPProperties, self).__init__()
    
        self.data['address'] = address
        self.data['alternateDnsServerAddress'] = alternateDnsServerAddress
        self.data['arpRedirectEnabled'] = arpRedirectEnabled
        self.data['defaultGateway'] = defaultGateway
        self.data['dhcpConfigurationEnabled'] = dhcpConfigurationEnabled
        self.data['ipv6Address'] = ipv6Address
        self.data['ipv6DefaultGateway'] = ipv6DefaultGateway
        self.data['ipv6SubnetMask'] = ipv6SubnetMask
        self.data['jumboFramesEnabled'] = jumboFramesEnabled
        self.data['mac'] = mac
        self.data['mtu'] = mtu
        self.data['primaryDnsServerAddress'] = primaryDnsServerAddress
        self.data['subnetMask'] = subnetMask
    
    
    @property
    def address(self):
        '''The current IPv4 address.
        '''
        return self.data['address']

    @property
    def alternateDnsServerAddress(self):
        '''The current secondary DNS address.
        '''
        return self.data['alternateDnsServerAddress']

    @property
    def arpRedirectEnabled(self):
        '''True if ARP Redirect is enabled
        '''
        return self.data['arpRedirectEnabled']

    @property
    def defaultGateway(self):
        '''The current IPv4 gateway.
        '''
        return self.data['defaultGateway']

    @property
    def dhcpConfigurationEnabled(self):
        '''True if the host bus adapter fetches its IP using DHCP.
        '''
        return self.data['dhcpConfigurationEnabled']

    @property
    def ipv6Address(self):
        '''The current IPv6 address.
        '''
        return self.data['ipv6Address']

    @property
    def ipv6DefaultGateway(self):
        '''The current IPv6 default gateway.
        '''
        return self.data['ipv6DefaultGateway']

    @property
    def ipv6SubnetMask(self):
        '''The current IPv6 subnet mask.
        '''
        return self.data['ipv6SubnetMask']

    @property
    def jumboFramesEnabled(self):
        '''vSphere API 4.0
        '''
        return self.data['jumboFramesEnabled']

    @property
    def mac(self):
        '''The MAC address.
        '''
        return self.data['mac']

    @property
    def mtu(self):
        '''True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc)
        Setting enableJumboFrames and not a numeric mtu value implies
        autoselection of appropriate MTU value for Jumbo Frames.
        '''
        return self.data['mtu']

    @property
    def primaryDnsServerAddress(self):
        '''The current primary DNS address.
        '''
        return self.data['primaryDnsServerAddress']

    @property
    def subnetMask(self):
        '''The current IPv4 subnet mask.
        '''
        return self.data['subnetMask']

