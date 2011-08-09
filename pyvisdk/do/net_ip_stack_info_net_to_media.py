
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpStackInfoNetToMedia(DynamicData):
    '''Information from an IP stack about known mappings betwwen an IP address and the
        underlying physical address it maps to as learned by: IPv4: Address
        Resolution Protocol (ARP) RFC 826 IPv6: Neighbor Discovery Protocol (NDP)
        RFC 4861
    '''
    
    def __init__(self, device, ipAddress, physicalAddress, type):
        # MUST define these
        super(NetIpStackInfoNetToMedia, self).__init__()
    
        self.data['device'] = device
        self.data['ipAddress'] = ipAddress
        self.data['physicalAddress'] = physicalAddress
        self.data['type'] = type
    
    
    @property
    def device(self):
        '''The value will be the name of the interface as reported by the operating system.
        '''
        return self.data['device']

    @property
    def ipAddress(self):
        '''A Unicast IP address of another system directly reachable w/o routing. IPv4
        address is specified using dotted decimal notation. For example,
        "192.0.2.1". IPv6 addresses are 128-bit addresses represented as eight
        fields of up to four hexadecimal digits. A colon separates each field (:).
        For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also
        consist of the symbol '::' to represent multiple 16-bit groups of
        contiguous 0's only once in an address as described in RFC 2373.
        '''
        return self.data['ipAddress']

    @property
    def physicalAddress(self):
        '''The media-dependent of the address or empty string if not yet learned. For
        Ethernet interfaces this is a MAC address reported in the format:
        XX:XX:XX:XX:XX:XX where XX are hexadecimal numbers.
        '''
        return self.data['physicalAddress']

    @property
    def type(self):
        '''The type/state of this entry as reported by the IP stack. See EntryType for
        values.
        '''
        return self.data['type']

