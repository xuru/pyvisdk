
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpConfig(DynamicData):
    '''The IP configuration.
    '''
    
    def __init__(self, dhcp, ipAddress, ipV6Config, subnetMask):
        # MUST define these
        super(HostIpConfig, self).__init__()
    
        self.data['dhcp'] = dhcp
        self.data['ipAddress'] = ipAddress
        self.data['ipV6Config'] = ipV6Config
        self.data['subnetMask'] = subnetMask
    
    
    @property
    def dhcp(self):
        '''The flag to indicate whether or not DHCP (dynamic host control protocol) is
        enabled. If this property is set to true, the ipAddress and the subnetMask
        strings cannot be set explicitly.
        '''
        return self.data['dhcp']

    @property
    def ipAddress(self):
        '''The IP address currently used by the network adapter. All IP addresses are
        specified using IPv4 dot notation. For example, "192.168.0.1". Subnet
        addresses and netmasks are specified using the same notation.
        '''
        return self.data['ipAddress']

    @property
    def ipV6Config(self):
        '''The ipv6 configuration
        '''
        return self.data['ipV6Config']

    @property
    def subnetMask(self):
        '''The subnet mask.
        '''
        return self.data['subnetMask']

