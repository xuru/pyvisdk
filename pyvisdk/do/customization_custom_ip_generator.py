
from pyvisdk.do.customization_ip_generator import CustomizationIpGenerator
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationCustomIpGenerator(CustomizationIpGenerator):
    '''Use a command-line program configured with the VirtualCenter server.
    '''
    
    def __init__(self, argument):
        # MUST define these
        super(CustomizationCustomIpGenerator, self).__init__()
    
        self.data['argument'] = argument
    
    
    @property
    def argument(self):
        '''An optional argument that is passed to the utility for this IP address. The
        meaning of this field is user-defined, in the script.
        '''
        return self.data['argument']

