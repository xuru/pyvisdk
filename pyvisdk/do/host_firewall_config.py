
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirewallConfig(DynamicData):
    '''DataObject used for firewall configuration
    '''
    
    def __init__(self, defaultBlockingPolicy, rule):
        # MUST define these
        super(HostFirewallConfig, self).__init__()
    
        self.data['defaultBlockingPolicy'] = defaultBlockingPolicy
        self.data['rule'] = rule
    
    
    @property
    def defaultBlockingPolicy(self):
        '''Default settings for the firewall, used for ports that are not explicitly opened.
        '''
        return self.data['defaultBlockingPolicy']

    @property
    def rule(self):
        '''Rules determining firewall settings.
        '''
        return self.data['rule']

