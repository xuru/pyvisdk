
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfilePolicy(DynamicData):
    '''This data object represents a policy.
    '''
    
    def __init__(self, id, policyOption):
        # MUST define these
        super(ProfilePolicy, self).__init__()
    
        self.data['id'] = id
        self.data['policyOption'] = policyOption
    
    
    @property
    def id(self):
        '''The id of Policy
        '''
        return self.data['id']

    @property
    def policyOption(self):
        '''The PolicyOption for the Policy. The 'id' of the PolicyOption should be among the
        values present in the possibleOption field of the Policy's metadata.
        '''
        return self.data['policyOption']

