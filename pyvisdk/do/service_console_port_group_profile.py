
from pyvisdk.do.port_group_profile import PortGroupProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ServiceConsolePortGroupProfile(PortGroupProfile):
    '''This data object type represents the profile for a Port Group that will be used by
        the Service Console.
    '''
    
    def __init__(self, ipConfig):
        # MUST define these
        super(ServiceConsolePortGroupProfile, self).__init__()
    
        self.data['ipConfig'] = ipConfig
    
    
    @property
    def ipConfig(self):
        '''The IP address configuration for the Service Console network
        '''
        return self.data['ipConfig']

