
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileUpdateFailedUpdateFailure(DynamicData):
    '''
    '''
    
    def __init__(self, errMsg, profilePath):
        # MUST define these
        super(ProfileUpdateFailedUpdateFailure, self).__init__()
    
        self.data['errMsg'] = errMsg
        self.data['profilePath'] = profilePath
    
    
    @property
    def errMsg(self):
        '''Message which explains the problem encountered
        '''
        return self.data['errMsg']

    @property
    def profilePath(self):
        '''Location in the profile which has the error
        '''
        return self.data['profilePath']

