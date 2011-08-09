
from pyvisdk.do.customization_ip_v6_generator import CustomizationIpV6Generator
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationCustomIpV6Generator(CustomizationIpV6Generator):
    '''Use a command-line program configured with the VirtualCenter server.
    '''
    
    def __init__(self, argument):
        # MUST define these
        super(CustomizationCustomIpV6Generator, self).__init__()
    
        self.data['argument'] = argument
    
    
    @property
    def argument(self):
        '''An optional argument that is passed to the utility for this ipv6 address. The
        meaning of this field is user-defined, in the script.
        '''
        return self.data['argument']

