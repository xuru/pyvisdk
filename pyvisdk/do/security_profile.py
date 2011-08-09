
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SecurityProfile(ApplyProfile):
    '''DataObject representing Security configurations of the host
    '''
    
    def __init__(self, permission):
        # MUST define these
        super(SecurityProfile, self).__init__()
    
        self.data['permission'] = permission
    
    
    @property
    def permission(self):
        '''Permission configuration
        '''
        return self.data['permission']

