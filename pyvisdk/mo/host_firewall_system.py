
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirewallSystem(ExtensibleManagedObject):
    '''The FirewallSystem managed object describes the firewall configuration of the
    host.The firewall should be configured first by setting the default policy and
    then by making exceptions to the policy to get the desired openness.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostFirewallSystem):
        super(HostFirewallSystem, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def firewallInfo(self):
        '''Firewall configuration.'''
        return self.update('firewallInfo')

    
    
    def DisableRuleset(self, id):
        '''Blocks the firewall ports belonging to the specified ruleset. If the ruleset
        has a managed service with a policy of 'auto' and all other rulesets used by
        the service are blocked, stops the service.
        
        :param id: 
        
        '''
        return self.delegate("DisableRuleset")(id)
    
    def EnableRuleset(self, id):
        '''Opens the firewall ports belonging to the specified ruleset. If the ruleset has
        a managed service with a policy of 'auto' that is not running, starts the
        service.
        
        :param id: 
        
        '''
        return self.delegate("EnableRuleset")(id)
    
    def RefreshFirewall(self):
        '''Refresh the firewall information and settings to pick up any changes made
        directly on the host.
        
        '''
        return self.delegate("RefreshFirewall")()
    
    def UpdateDefaultPolicy(self, defaultPolicy):
        '''Updates the default firewall policy; unset fields are left unchanged.
        
        :param defaultPolicy: 
        
        '''
        return self.delegate("UpdateDefaultPolicy")(defaultPolicy)
    
    def UpdateRuleset(self, id, spec):
        '''Update the firewall ruleset specification.
        
        :param id: 
        
        :param spec: 
        
        '''
        return self.delegate("UpdateRuleset")(id, spec)