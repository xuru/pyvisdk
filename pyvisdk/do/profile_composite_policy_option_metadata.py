
from pyvisdk.do.profile_policy_option_metadata import ProfilePolicyOptionMetadata
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileCompositePolicyOptionMetadata(ProfilePolicyOptionMetadata):
    '''DataObject represents the metadata information of a composite PolicyOption. The
        user will retrieve the metadata information about a composite policy and
        then compose the Composite PolicyOption.
    '''
    
    def __init__(self, option):
        # MUST define these
        super(ProfileCompositePolicyOptionMetadata, self).__init__()
    
        self.data['option'] = option
    
    
    @property
    def option(self):
        '''List of optional policy option identifiers that could be composed in this
        composite policy option. The policyOptions should already be part of the
        possible policyOptions for the policy.
        '''
        return self.data['option']

