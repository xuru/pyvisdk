
from pyvisdk.do.customization_ip_generator import CustomizationIpGenerator
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationFixedIp(CustomizationIpGenerator):
    '''Use a static IP Address for the virtual network adapter.
    '''
    
    def __init__(self, ipAddress):
        # MUST define these
        super(CustomizationFixedIp, self).__init__()
    
        self.data['ipAddress'] = ipAddress
    
    
    @property
    def ipAddress(self):
        '''
        '''
        return self.data['ipAddress']

