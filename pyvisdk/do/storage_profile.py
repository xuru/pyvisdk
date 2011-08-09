
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StorageProfile(ApplyProfile):
    '''DataObject representing the storage configuration
    '''
    
    def __init__(self, nasStorage):
        # MUST define these
        super(StorageProfile, self).__init__()
    
        self.data['nasStorage'] = nasStorage
    
    
    @property
    def nasStorage(self):
        '''The set of NAS storage profiles.
        '''
        return self.data['nasStorage']

