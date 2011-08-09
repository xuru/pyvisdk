
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FirewallProfile(ApplyProfile):
    '''DataObject representing the Firewall configuration on the host
    '''
    
    def __init__(self, ruleset):
        # MUST define these
        super(FirewallProfile, self).__init__()
    
        self.data['ruleset'] = ruleset
    
    
    @property
    def ruleset(self):
        '''List of Rulesets that will be configured for the profile.
        '''
        return self.data['ruleset']

