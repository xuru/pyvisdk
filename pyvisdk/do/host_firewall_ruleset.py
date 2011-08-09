
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirewallRuleset(DynamicData):
    '''Data object that describes a single network ruleset that can be allowed or blocked
        by the firewall using the HostFirewallSystem object.
    '''
    
    def __init__(self, enabled, key, label, required, rule, service):
        # MUST define these
        super(HostFirewallRuleset, self).__init__()
    
        self.data['enabled'] = enabled
        self.data['key'] = key
        self.data['label'] = label
        self.data['required'] = required
        self.data['rule'] = rule
        self.data['service'] = service
    
    
    @property
    def enabled(self):
        '''Flag indicating whether the ruleset is enabled. If the ruleset is enabled, all
        ports specified in the ruleset are opened by the firewall.
        '''
        return self.data['enabled']

    @property
    def key(self):
        '''Brief identifier for the ruleset.
        '''
        return self.data['key']

    @property
    def label(self):
        '''Display label for the ruleset.
        '''
        return self.data['label']

    @property
    def required(self):
        '''Flag indicating whether the ruleset is required and cannot be disabled.
        '''
        return self.data['required']

    @property
    def rule(self):
        '''List of rules within the ruleset.
        '''
        return self.data['rule']

    @property
    def service(self):
        '''Managed service (if any) that uses this ruleset. Must be one of the services
        listed in service.
        '''
        return self.data['service']

