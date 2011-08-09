
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfilePropertyPath(DynamicData):
    '''DataObject representing the path to either a Profile or a Policy.
    '''
    
    def __init__(self, policyId, profilePath):
        # MUST define these
        super(ProfilePropertyPath, self).__init__()
    
        self.data['policyId'] = policyId
        self.data['profilePath'] = profilePath
    
    
    @property
    def policyId(self):
        '''Id of the Policy part
        '''
        return self.data['policyId']

    @property
    def profilePath(self):
        '''Complete path to the leaf profile
        '''
        return self.data['profilePath']

