
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicProfile(ApplyProfile):
    '''DataObject representing configurations of a Physical Nic
    '''
    
    def __init__(self, key):
        # MUST define these
        super(PhysicalNicProfile, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''The linkable identifier
        '''
        return self.data['key']

