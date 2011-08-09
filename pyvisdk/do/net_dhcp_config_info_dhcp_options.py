
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetDhcpConfigInfoDhcpOptions(DynamicData):
    '''Provides for reporting of DHCP client. This data object may be used at a per
        interface or per system scope.
    '''
    
    def __init__(self, config, enable):
        # MUST define these
        super(NetDhcpConfigInfoDhcpOptions, self).__init__()
    
        self.data['config'] = config
        self.data['enable'] = enable
    
    
    @property
    def config(self):
        '''Platform specific settings for DHCP Client. The key part is a unique number, the
        value part is the platform specific configuration command. For example on
        Linux, BSD systems using the file dhclient.conf output would be reported
        at system scope: key='1', value='timeout 60;' key='2', value='reboot 10;'
        output reported at per interface scope: key='1', value='prepend domain-
        name-servers 192.0.2.1;' key='2', value='equire subnet-mask, domain-name-
        servers;'
        '''
        return self.data['config']

    @property
    def enable(self):
        '''Report state of dhcp client services.
        '''
        return self.data['enable']

