
from pyvisdk.do.customization_name import CustomizationName
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationCustomName(CustomizationName):
    '''Specifies that the VirtualCenter server will launch an external application to
        generate the (hostname/IP). The command line for this application must be
        specified in the server configuration file (vpxd.cfg) in the vpxd/name-ip-
        generator key.
    '''
    
    def __init__(self, argument):
        # MUST define these
        super(CustomizationCustomName, self).__init__()
    
        self.data['argument'] = argument
    
    
    @property
    def argument(self):
        '''An optional argument that is passed to the utility for this IP address. The
        meaning of this field is user-defined in the script.
        '''
        return self.data['argument']

