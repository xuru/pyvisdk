
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpConfigInfoIpAddress(DynamicData):
    '''Information about a specific IP Address.
    '''
    
    def __init__(self, ipAddress, lifetime, origin, prefixLength, state):
        # MUST define these
        super(NetIpConfigInfoIpAddress, self).__init__()
    
        self.data['ipAddress'] = ipAddress
        self.data['lifetime'] = lifetime
        self.data['origin'] = origin
        self.data['prefixLength'] = prefixLength
        self.data['state'] = state
    
    
    @property
    def ipAddress(self):
        '''IPv4 address is specified using dotted decimal notation. For example, "192.0.2.1".
        IPv6 addresses are 128-bit addresses represented as eight fields of up to
        four hexadecimal digits. A colon separates each field (:). For example,
        2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the
        symbol '::' to represent multiple 16-bit groups of contiguous 0's only
        once in an address as described in RFC 2373.
        '''
        return self.data['ipAddress']

    @property
    def lifetime(self):
        '''The time when will this address expire. Durning this time state may change states
        but is still visible from the network.
        '''
        return self.data['lifetime']

    @property
    def origin(self):
        '''How this address was configured. This can be one of the values from the enum
        IpAddressOrigin See IpAddressOrigin for values.
        '''
        return self.data['origin']

    @property
    def prefixLength(self):
        '''Denotes the length of a generic Internet network address prefix. The prefix length
        for IPv4 the value range is 0-32. For IPv6 prefixLength is a decimal value
        range 0-128. A value of n corresponds to an IP address mask that has n
        contiguous 1-bits from the most significant bit (MSB), with all other bits
        set to 0. A value of zero is valid only if the calling context defines it.
        '''
        return self.data['prefixLength']

    @property
    def state(self):
        '''The state of this ipAddress. Can be one of IpAddressStatus.
        '''
        return self.data['state']

