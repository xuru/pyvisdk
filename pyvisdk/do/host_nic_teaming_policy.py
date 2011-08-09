
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNicTeamingPolicy(DynamicData):
    '''Policy for a network adapter team.
    '''
    
    def __init__(self, failureCriteria, nicOrder, notifySwitches, policy, reversePolicy, rollingOrder):
        # MUST define these
        super(HostNicTeamingPolicy, self).__init__()
    
        self.data['failureCriteria'] = failureCriteria
        self.data['nicOrder'] = nicOrder
        self.data['notifySwitches'] = notifySwitches
        self.data['policy'] = policy
        self.data['reversePolicy'] = reversePolicy
        self.data['rollingOrder'] = rollingOrder
    
    
    @property
    def failureCriteria(self):
        '''Failover detection policy for this network adapter team. The bridge must be
        BondBridge for this property to be valid.
        '''
        return self.data['failureCriteria']

    @property
    def nicOrder(self):
        '''Failover order policy for network adapters on this switch. The bridge must be
        BondBridge for this property to be valid.
        '''
        return self.data['nicOrder']

    @property
    def notifySwitches(self):
        '''Flag to specify whether or not to notify the physical switch if a link fails. If
        this property is true, ESX Server will respond to the failure by sending a
        RARP packet from a different physical adapter, causing the switch to
        update its cache.
        '''
        return self.data['notifySwitches']

    @property
    def policy(self):
        '''Network adapter teaming policy includes failover and load balancing, It can be one
        of the following: *
        '''
        return self.data['policy']

    @property
    def reversePolicy(self):
        '''The flag to indicate whether or not the teaming policy is applied to inbound
        frames as well. For example, if the policy is explicit failover, a
        broadcast request goes through uplink1 and comes back through uplink2.
        Then if the reverse policy is set, the frame is dropped when it is
        received from uplink2. This reverse policy is useful to prevent the
        virtual machine from getting reflections.
        '''
        return self.data['reversePolicy']

    @property
    def rollingOrder(self):
        '''The flag to indicate whether or not to use a rolling policy when restoring links.
        For example, assume the explicit link order is (vmnic9, vmnic0), therefore
        vmnic9 goes down, vmnic0 comes up. However, when vmnic9 comes backup, if
        rollingOrder is set to be true, vmnic0 continues to be used, otherwise,
        vmnic9 is restored as specified in the explicitly order.
        '''
        return self.data['rollingOrder']

