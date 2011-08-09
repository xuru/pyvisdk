
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpRouteConfig(DynamicData):
    '''IP Route Configuration. All IPv4 addresses, subnet addresses, and netmasks are
        specified as strings using dotted decimal notation. For example,
        "192.0.2.1". IPv6 addresses are 128-bit addresses represented as eight
        fields of up to four hexadecimal digits. A colon separates each field (:).
        For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also
        consist of symbol '::' to represent multiple 16-bit groups of contiguous
        0's only once in an address as described in RFC 2373.
    '''
    
    def __init__(self, defaultGateway, gatewayDevice, ipV6DefaultGateway, ipV6GatewayDevice):
        # MUST define these
        super(HostIpRouteConfig, self).__init__()
    
        self.data['defaultGateway'] = defaultGateway
        self.data['gatewayDevice'] = gatewayDevice
        self.data['ipV6DefaultGateway'] = ipV6DefaultGateway
        self.data['ipV6GatewayDevice'] = ipV6GatewayDevice
    
    
    @property
    def defaultGateway(self):
        '''The default gateway address.
        '''
        return self.data['defaultGateway']

    @property
    def gatewayDevice(self):
        '''The gateway device. This applies to service console gateway only, it is ignored
        otherwise.
        '''
        return self.data['gatewayDevice']

    @property
    def ipV6DefaultGateway(self):
        '''The default ipv6 gateway address
        '''
        return self.data['ipV6DefaultGateway']

    @property
    def ipV6GatewayDevice(self):
        '''The ipv6 gateway device. This applies to service console gateway only, it
        '''
        return self.data['ipV6GatewayDevice']

