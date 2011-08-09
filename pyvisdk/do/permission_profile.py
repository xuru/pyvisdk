
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PermissionProfile(ApplyProfile):
    '''This data object type represents the profile for a permission rule
    '''
    
    def __init__(self, key):
        # MUST define these
        super(PermissionProfile, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''
        '''
        return self.data['key']

