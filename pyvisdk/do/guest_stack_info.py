
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestStackInfo(DynamicData):
    '''Information about the Internet Protocol stack as configured in the guest operating
        system.
    '''
    
    def __init__(self, dhcpConfig, dnsConfig, ipRouteConfig, ipStackConfig):
        # MUST define these
        super(GuestStackInfo, self).__init__()
    
        self.data['dhcpConfig'] = dhcpConfig
        self.data['dnsConfig'] = dnsConfig
        self.data['ipRouteConfig'] = ipRouteConfig
        self.data['ipStackConfig'] = ipStackConfig
    
    
    @property
    def dhcpConfig(self):
        '''Client side DHCP for a given interface. This reports only the system wide dhcp
        client settings. See NicInfo.IpConfig for per interface settings. For
        example on Linux, BSD systems: Using the file dhclient.conf output would
        be reported as: key='1', value='timeout 60;' key='2', value='reboot 10;'
        '''
        return self.data['dhcpConfig']

    @property
    def dnsConfig(self):
        '''Client DNS configuration. How DNS queries are resolved.
        '''
        return self.data['dnsConfig']

    @property
    def ipRouteConfig(self):
        '''IP route table configuration.
        '''
        return self.data['ipRouteConfig']

    @property
    def ipStackConfig(self):
        '''Report Kernel IP configuration settings. The key part contains a unique number in
        the report. The value part contains the 'key=value' as provided by the
        underlying provider. For example on Linux, BSD, the systcl -a output would
        be reported as: key='5', value='net.ipv4.tcp_keepalive_time = 7200'
        '''
        return self.data['ipStackConfig']

