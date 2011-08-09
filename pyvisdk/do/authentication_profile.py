
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AuthenticationProfile(ApplyProfile):
    '''This data object type represents the profile for authentication configuration
    '''
    
    def __init__(self, activeDirectory):
        # MUST define these
        super(AuthenticationProfile, self).__init__()
    
        self.data['activeDirectory'] = activeDirectory
    
    
    @property
    def activeDirectory(self):
        '''Profile representing the Active Directory configuration
        '''
        return self.data['activeDirectory']

