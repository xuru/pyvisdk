
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpRouteConfigSpecIpRouteSpec(DynamicData):
    '''Specify an individual host, network or default destination network reachable
        through a given gateway.
    '''
    
    def __init__(self, gateway, network, operation, prefixLength):
        # MUST define these
        super(NetIpRouteConfigSpecIpRouteSpec, self).__init__()
    
        self.data['gateway'] = gateway
        self.data['network'] = network
        self.data['operation'] = operation
        self.data['prefixLength'] = prefixLength
    
    
    @property
    def gateway(self):
        '''Where to send the packets for this route.
        '''
        return self.data['gateway']

    @property
    def network(self):
        '''IP Address of the destination IP network. IPv6 addresses are 128-bit addresses
        represented as eight fields of up to four hexadecimal digits. A colon
        separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff.
        The address can also consist of symbol '::' to represent multiple 16-bit
        groups of contiguous 0's only once in an address as described in RFC 2373.
        To Specify a default network use the value: 0 with prefixLenth 0.
        '''
        return self.data['network']

    @property
    def operation(self):
        '''Requires one of the values from HostConfigChangeOperation.
        '''
        return self.data['operation']

    @property
    def prefixLength(self):
        '''The prefix length. For IPv4 the value range is 0-31. For IPv6 prefixLength is a
        decimal value range 0-127. The property represents the number of
        contiguous, higher-order bits of the address that make up the network
        portion of the IP address.
        '''
        return self.data['prefixLength']

