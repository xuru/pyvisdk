
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpConfigIpV6Address(DynamicData):
    '''The ipv6 address specification
    '''
    
    def __init__(self, dadState, ipAddress, lifetime, operation, origin, prefixLength):
        # MUST define these
        super(HostIpConfigIpV6Address, self).__init__()
    
        self.data['dadState'] = dadState
        self.data['ipAddress'] = ipAddress
        self.data['lifetime'] = lifetime
        self.data['operation'] = operation
        self.data['origin'] = origin
        self.data['prefixLength'] = prefixLength
    
    
    @property
    def dadState(self):
        '''The state of this ipAddress. Can be one of HostIpConfigIpV6AddressStatus
        '''
        return self.data['dadState']

    @property
    def ipAddress(self):
        '''The ipv6 address. When DHCP is enabled, this property reflects the current IP
        configuration and cannot be set.
        '''
        return self.data['ipAddress']

    @property
    def lifetime(self):
        '''The time when will this address expire. If not set the address lifetime is
        unlimited.
        '''
        return self.data['lifetime']

    @property
    def operation(self):
        '''Valid values are "add" and "remove". See HostConfigChangeOperation.
        '''
        return self.data['operation']

    @property
    def origin(self):
        '''The type of the ipv6 address configuration on the interface. This can be one of
        the types defined my the enum HostIpConfigIpV6AddressConfigType.
        '''
        return self.data['origin']

    @property
    def prefixLength(self):
        '''The prefix length. An ipv6 prefixLength is a decimal value that indicates the
        number of contiguous, higher-order bits of the address that make up the
        network portion of the address. For example, 10FA:6604:8136:6502::/64 is a
        possible IPv6 prefix. The prefix length in this case is 64.
        '''
        return self.data['prefixLength']

