
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class IpPoolIpPoolConfigInfo(DynamicData):
    '''Specifications of either IPv4 or IPv6 configuration to be used on this network.
        This is a part of network configuration.IPv4 addresses are in dot-decimal
        notation, e.g.: 192.0.2.235IPv6 addresses are in colon-hexadecimal
        notation, e.g.: 2001:0db8:85a3::0370:7334
    '''
    
    def __init__(self, dhcpServerAvailable, dns, gateway, ipPoolEnabled, netmask, range, subnetAddress):
        # MUST define these
        super(IpPoolIpPoolConfigInfo, self).__init__()
    
        self.data['dhcpServerAvailable'] = dhcpServerAvailable
        self.data['dns'] = dns
        self.data['gateway'] = gateway
        self.data['ipPoolEnabled'] = ipPoolEnabled
        self.data['netmask'] = netmask
        self.data['range'] = range
        self.data['subnetAddress'] = subnetAddress
    
    
    @property
    def dhcpServerAvailable(self):
        '''Whether a DHCP server is available on this network.
        '''
        return self.data['dhcpServerAvailable']

    @property
    def dns(self):
        '''DNS servers
        '''
        return self.data['dns']

    @property
    def gateway(self):
        '''Gateway. This can be an empty string - if no gateway is configured.
        '''
        return self.data['gateway']

    @property
    def ipPoolEnabled(self):
        '''IP addresses can only be allocated from the range if the IP pool is enabled.
        '''
        return self.data['ipPoolEnabled']

    @property
    def netmask(self):
        '''Netmask
        '''
        return self.data['netmask']

    @property
    def range(self):
        '''IP range. This is specified as a set of ranges separated with commas. One range is
        given by a start address, a hash (#), and the length of the range.
        '''
        return self.data['range']

    @property
    def subnetAddress(self):
        '''Address of the subnet.
        '''
        return self.data['subnetAddress']

