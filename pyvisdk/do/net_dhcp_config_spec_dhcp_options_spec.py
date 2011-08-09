
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetDhcpConfigSpecDhcpOptionsSpec(DynamicData):
    '''Provides for configuration of IPv6
    '''
    
    def __init__(self, config, enable, operation):
        # MUST define these
        super(NetDhcpConfigSpecDhcpOptionsSpec, self).__init__()
    
        self.data['config'] = config
        self.data['enable'] = enable
        self.data['operation'] = operation
    
    
    @property
    def config(self):
        '''Platform specific settings for DHCP Client. The key part is a unique number, the
        value part is the platform specific configuration command. See
        NetDhcpConfigInfo for value formatting.
        '''
        return self.data['config']

    @property
    def enable(self):
        '''Enable or disable dhcp for IPv4.
        '''
        return self.data['enable']

    @property
    def operation(self):
        '''Requires one of the values from HostConfigChangeOperation.
        '''
        return self.data['operation']

