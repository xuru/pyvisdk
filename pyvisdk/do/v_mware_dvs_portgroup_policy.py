
from pyvisdk.do.dv_portgroup_policy import DVPortgroupPolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMwareDVSPortgroupPolicy(DVPortgroupPolicy):
    '''This class defines the VMware specific configuration for DistributedVirtualPort.
    '''
    
    def __init__(self, securityPolicyOverrideAllowed, uplinkTeamingOverrideAllowed, vlanOverrideAllowed):
        # MUST define these
        super(VMwareDVSPortgroupPolicy, self).__init__()
    
        self.data['securityPolicyOverrideAllowed'] = securityPolicyOverrideAllowed
        self.data['uplinkTeamingOverrideAllowed'] = uplinkTeamingOverrideAllowed
        self.data['vlanOverrideAllowed'] = vlanOverrideAllowed
    
    
    @property
    def securityPolicyOverrideAllowed(self):
        '''Allow the setting of securityPolicy for an individual port to override the setting
        in defaultPortConfig of a portgroup.
        '''
        return self.data['securityPolicyOverrideAllowed']

    @property
    def uplinkTeamingOverrideAllowed(self):
        '''Allow the setting of uplinkTeamingPolicy for an individual port to override the
        setting in defaultPortConfig of a portgroup.
        '''
        return self.data['uplinkTeamingOverrideAllowed']

    @property
    def vlanOverrideAllowed(self):
        '''Allow the setting of vlanId, trunk vlanId, or pvlanId for an individual port to
        override the setting in defaultPortConfig of a portgroup.
        '''
        return self.data['vlanOverrideAllowed']

