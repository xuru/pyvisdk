
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirewallInfo(DynamicData):
    '''Data object describing the firewall configuration.
    '''
    
    def __init__(self, defaultPolicy, ruleset):
        # MUST define these
        super(HostFirewallInfo, self).__init__()
    
        self.data['defaultPolicy'] = defaultPolicy
        self.data['ruleset'] = ruleset
    
    
    @property
    def defaultPolicy(self):
        '''Default firewall policy.
        '''
        return self.data['defaultPolicy']

    @property
    def ruleset(self):
        '''List of configured rulesets.
        '''
        return self.data['ruleset']

