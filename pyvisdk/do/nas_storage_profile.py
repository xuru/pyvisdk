
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NasStorageProfile(ApplyProfile):
    '''DataObject representing configuration of one NAS datastore.
    '''
    
    def __init__(self, key):
        # MUST define these
        super(NasStorageProfile, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''The linkable identifier
        '''
        return self.data['key']

