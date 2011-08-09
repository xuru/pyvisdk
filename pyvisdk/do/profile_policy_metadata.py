
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfilePolicyMetadata(DynamicData):
    '''This data object represents the metadata information of a Policy
    '''
    
    def __init__(self, id, possibleOption):
        # MUST define these
        super(ProfilePolicyMetadata, self).__init__()
    
        self.data['id'] = id
        self.data['possibleOption'] = possibleOption
    
    
    @property
    def id(self):
        '''Identifier of the Policy.
        '''
        return self.data['id']

    @property
    def possibleOption(self):
        '''The possible policy options that can be set for a policy of the given kind.
        '''
        return self.data['possibleOption']

