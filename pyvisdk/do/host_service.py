
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostService(DynamicData):
    '''Data object that describes a single service that runs on the host.
    '''
    
    def __init__(self, key, label, policy, required, ruleset, running, uninstallable):
        # MUST define these
        super(HostService, self).__init__()
    
        self.data['key'] = key
        self.data['label'] = label
        self.data['policy'] = policy
        self.data['required'] = required
        self.data['ruleset'] = ruleset
        self.data['running'] = running
        self.data['uninstallable'] = uninstallable
    
    
    @property
    def key(self):
        '''Brief identifier for the service.
        '''
        return self.data['key']

    @property
    def label(self):
        '''Display label for the service.
        '''
        return self.data['label']

    @property
    def policy(self):
        '''Service activation policy.
        '''
        return self.data['policy']

    @property
    def required(self):
        '''Flag indicating whether the service is required and cannot be disabled.
        '''
        return self.data['required']

    @property
    def ruleset(self):
        '''List of firewall rulesets used by this service. Must come from the list of
        rulesets in ruleset.
        '''
        return self.data['ruleset']

    @property
    def running(self):
        '''Flag indicating whether the service is currently running.
        '''
        return self.data['running']

    @property
    def uninstallable(self):
        '''Flag indicating whether the service can be uninstalled.
        '''
        return self.data['uninstallable']

