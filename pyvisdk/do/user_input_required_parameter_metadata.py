
from pyvisdk.do.profile_policy_option_metadata import ProfilePolicyOptionMetadata
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserInputRequiredParameterMetadata(ProfilePolicyOptionMetadata):
    '''DataObject represents the metadata information for a parameter which will be
        specified by the user during apply time.
    '''
    
    def __init__(self, userInputParameter):
        # MUST define these
        super(UserInputRequiredParameterMetadata, self).__init__()
    
        self.data['userInputParameter'] = userInputParameter
    
    
    @property
    def userInputParameter(self):
        '''
        '''
        return self.data['userInputParameter']

