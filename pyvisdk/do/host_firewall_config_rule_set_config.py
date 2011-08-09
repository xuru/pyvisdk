
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirewallConfigRuleSetConfig(DynamicData):
    '''
    '''
    
    def __init__(self, enabled, rulesetId):
        # MUST define these
        super(HostFirewallConfigRuleSetConfig, self).__init__()
    
        self.data['enabled'] = enabled
        self.data['rulesetId'] = rulesetId
    
    
    @property
    def enabled(self):
        '''Flag indicating if the specified ruleset should be enabled.
        '''
        return self.data['enabled']

    @property
    def rulesetId(self):
        '''Id of the ruleset.
        '''
        return self.data['rulesetId']

