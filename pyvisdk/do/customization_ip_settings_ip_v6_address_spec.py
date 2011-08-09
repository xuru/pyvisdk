
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationIPSettingsIpV6AddressSpec(DynamicData):
    '''IPv6 settings
    '''
    
    def __init__(self, gateway, ip):
        # MUST define these
        super(CustomizationIPSettingsIpV6AddressSpec, self).__init__()
    
        self.data['gateway'] = gateway
        self.data['ip'] = ip
    
    
    @property
    def gateway(self):
        '''gateways
        '''
        return self.data['gateway']

    @property
    def ip(self):
        '''ipv6 address generators
        '''
        return self.data['ip']

