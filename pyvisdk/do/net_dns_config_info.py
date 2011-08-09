
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetDnsConfigInfo(DynamicData):
    '''Domain Name Server (DNS) Configuration Specification - a data object for reporting
        the configuration of RFC 1034 client side DNS settings.
    '''
    
    def __init__(self, dhcp, domainName, hostName, ipAddress, searchDomain):
        # MUST define these
        super(NetDnsConfigInfo, self).__init__()
    
        self.data['dhcp'] = dhcp
        self.data['domainName'] = domainName
        self.data['hostName'] = hostName
        self.data['ipAddress'] = ipAddress
        self.data['searchDomain'] = searchDomain
    
    
    @property
    def dhcp(self):
        '''Indicates whether or not dynamic host control protocol (DHCP) is used to configure
        DNS configuration.
        '''
        return self.data['dhcp']

    @property
    def domainName(self):
        '''The domain name portion of the DNS name. "example.com" part of esx01.example.com.
        '''
        return self.data['domainName']

    @property
    def hostName(self):
        '''The host name portion of DNS name. For example, "esx01" part of esx01.example.com.
        '''
        return self.data['hostName']

    @property
    def ipAddress(self):
        '''The IP addresses of the DNS servers in order of use. IPv4 addresses are specified
        using dotted decimal notation. For example, "192.0.2.1". IPv6 addresses
        are 128-bit addresses represented as eight fields of up to four
        hexadecimal digits. A colon separates each field (:). For example,
        2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the
        symbol '::' to represent multiple 16-bit groups of contiguous 0's only
        once in an address as described in RFC 2373.
        '''
        return self.data['ipAddress']

    @property
    def searchDomain(self):
        '''The domain in which to search for hosts, placed in order of preference.
        '''
        return self.data['searchDomain']

