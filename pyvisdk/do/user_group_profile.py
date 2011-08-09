
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserGroupProfile(ApplyProfile):
    '''DataObject representing a UserGroup
    '''
    
    def __init__(self, key):
        # MUST define these
        super(UserGroupProfile, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''The linkable identifier
        '''
        return self.data['key']

