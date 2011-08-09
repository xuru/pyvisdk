
from pyvisdk.do.host_profile_config_spec import HostProfileConfigSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfileHostBasedConfigSpec(HostProfileConfigSpec):
    '''DataObject which defines the configSpec when HostProfile is being created or
        updated from a Host.
    '''
    
    def __init__(self, host):
        # MUST define these
        super(HostProfileHostBasedConfigSpec, self).__init__()
    
        self.data['host'] = host
    
    
    @property
    def host(self):
        '''
        '''
        return self.data['host']

