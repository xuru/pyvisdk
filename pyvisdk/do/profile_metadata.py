
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileMetadata(DynamicData):
    '''This data object represents the metadata information of a Profile.
    '''
    
    def __init__(self, description, key):
        # MUST define these
        super(ProfileMetadata, self).__init__()
    
        self.data['description'] = description
        self.data['key'] = key
    
    
    @property
    def description(self):
        '''Property which describes the profile
        '''
        return self.data['description']

    @property
    def key(self):
        '''Type of the Profile
        '''
        return self.data['key']

