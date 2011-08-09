
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsVNicProfile(ApplyProfile):
    '''
    '''
    
    def __init__(self, ipConfig, key):
        # MUST define these
        super(DvsVNicProfile, self).__init__()
    
        self.data['ipConfig'] = ipConfig
        self.data['key'] = key
    
    
    @property
    def ipConfig(self):
        '''IP address for DVS VNic
        '''
        return self.data['ipConfig']

    @property
    def key(self):
        '''The linkable identifier
        '''
        return self.data['key']

