
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ApplyProfile(DynamicData):
    '''This data object type is the base class for all profiles.
    '''
    
    def __init__(self, enabled, policy):
        # MUST define these
        super(ApplyProfile, self).__init__()
    
        self.data['enabled'] = enabled
        self.data['policy'] = policy
    
    
    @property
    def enabled(self):
        '''Indicates whether the profile is enabled.
        '''
        return self.data['enabled']

    @property
    def policy(self):
        '''The list of policies comprising the profile.
        '''
        return self.data['policy']

