
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDnsConfig(DynamicData):
    '''This data object type describes the DNS configuration.All IPv4 addresses, subnet
        addresses, and netmasks are specified using dotted decimal notation. For
        example, "192.0.2.1". IPv6 addresses are 128-bit addresses represented as
        eight fields of up to four hexadecimal digits. A colon separates each
        field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can
        also consist of the symbol '::' to represent multiple 16-bit groups of
        contiguous 0's only once in an address as described in RFC 2373.
    '''
    
    def __init__(self, address, dhcp, domainName, hostName, searchDomain, virtualNicDevice):
        # MUST define these
        super(HostDnsConfig, self).__init__()
    
        self.data['address'] = address
        self.data['dhcp'] = dhcp
        self.data['domainName'] = domainName
        self.data['hostName'] = hostName
        self.data['searchDomain'] = searchDomain
        self.data['virtualNicDevice'] = virtualNicDevice
    
    
    @property
    def address(self):
        '''The IP addresses of the DNS servers, placed in order of preference.
        '''
        return self.data['address']

    @property
    def dhcp(self):
        '''The flag to indicate whether or not DHCP (dynamic host control protocol) is used
        to determine DNS configuration automatically.
        '''
        return self.data['dhcp']

    @property
    def domainName(self):
        '''The domain name portion of the DNS name. For example, "vmware.com".
        '''
        return self.data['domainName']

    @property
    def hostName(self):
        '''The host name portion of DNS name. For example, "esx01".
        '''
        return self.data['hostName']

    @property
    def searchDomain(self):
        '''The domain in which to search for hosts, placed in order of preference.
        '''
        return self.data['searchDomain']

    @property
    def virtualNicDevice(self):
        '''If DHCP is enabled, the DHCP DNS of the service console network adapter will
        override the system DNS. This field is ignored if DHCP is disabled by the
        dhcp property.
        '''
        return self.data['virtualNicDevice']

