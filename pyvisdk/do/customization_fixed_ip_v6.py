
from pyvisdk.do.customization_ip_v6_generator import CustomizationIpV6Generator
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationFixedIpV6(CustomizationIpV6Generator):
    '''Use a static ipv6 address for the virtual network adapter
    '''
    
    def __init__(self, ipAddress, subnetMask):
        # MUST define these
        super(CustomizationFixedIpV6, self).__init__()
    
        self.data['ipAddress'] = ipAddress
        self.data['subnetMask'] = subnetMask
    
    
    @property
    def ipAddress(self):
        '''
        '''
        return self.data['ipAddress']

    @property
    def subnetMask(self):
        '''
        '''
        return self.data['subnetMask']

