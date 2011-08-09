
from pyvisdk.do.inheritable_policy import InheritablePolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmwareUplinkPortTeamingPolicy(InheritablePolicy):
    '''Policy for a uplink port team.
    '''
    
    def __init__(self, failureCriteria, notifySwitches, policy, reversePolicy, rollingOrder, uplinkPortOrder):
        # MUST define these
        super(VmwareUplinkPortTeamingPolicy, self).__init__()
    
        self.data['failureCriteria'] = failureCriteria
        self.data['notifySwitches'] = notifySwitches
        self.data['policy'] = policy
        self.data['reversePolicy'] = reversePolicy
        self.data['rollingOrder'] = rollingOrder
        self.data['uplinkPortOrder'] = uplinkPortOrder
    
    
    @property
    def failureCriteria(self):
        '''Failover detection policy for the uplink port team.
        '''
        return self.data['failureCriteria']

    @property
    def notifySwitches(self):
        '''Flag to specify whether or not to notify the physical switch if a link fails. Also
        see notifySwitches
        '''
        return self.data['notifySwitches']

    @property
    def policy(self):
        '''Network adapter teaming policy. The policy defines the way traffic from the
        clients of the team is routed through the different uplinks in the team.
        The policies supported on the vDS platform is one of nicTeamingPolicy.
        '''
        return self.data['policy']

    @property
    def reversePolicy(self):
        '''The flag to indicate whether or not the teaming policy is applied to inbound
        frames as well. Also see reversePolicy
        '''
        return self.data['reversePolicy']

    @property
    def rollingOrder(self):
        '''The flag to indicate whether or not to use a rolling policy when restoring links.
        Also see rollingOrder
        '''
        return self.data['rollingOrder']

    @property
    def uplinkPortOrder(self):
        '''Failover order policy for uplink ports on the hosts.
        '''
        return self.data['uplinkPortOrder']

