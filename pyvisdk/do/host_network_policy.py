
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNetworkPolicy(DynamicData):
    '''This data object type describes network policies that can be configured for both
        virtual switches and port groups. The policy settings on the port group
        can inherit policy settings from their containing virtual switch. These
        policy settings are inherited if the settings on the port group are not
        set. Since every policy setting on a port group is optional, every
        individual policy setting can be inherited.By contrast, if a host is
        capable of implementing a policy setting, every virtual switch has some
        value assigned to the policy setting. In this case, although all of the
        policy settings are optional, they always have some value either by
        inheritance or by direct setting.Policy settings are organized into policy
        groups such as SecurityPolicy. Policy groups are optional since it is
        possible that a host may not implement such policies. If a host does not
        support a policy group, the policy group is not set on both the virtual
        switches and the port groups. See HostNetCapabilities
    '''
    
    def __init__(self, nicTeaming, offloadPolicy, security, shapingPolicy):
        # MUST define these
        super(HostNetworkPolicy, self).__init__()
    
        self.data['nicTeaming'] = nicTeaming
        self.data['offloadPolicy'] = offloadPolicy
        self.data['security'] = security
        self.data['shapingPolicy'] = shapingPolicy
    
    
    @property
    def nicTeaming(self):
        '''The network adapter teaming policy. The bridge must be BondBridge for this
        property to be valid.
        '''
        return self.data['nicTeaming']

    @property
    def offloadPolicy(self):
        '''Offload capabilities are used to optimize virtual machine network performance.
        When a virtual machine is transmitting on a network, some operations can
        be offloaded to either the host or the physical hardware. This policy
        indicates what networking related operations should be offloaded.
        '''
        return self.data['offloadPolicy']

    @property
    def security(self):
        '''The security policy governing ports on this virtual switch.
        '''
        return self.data['security']

    @property
    def shapingPolicy(self):
        '''The traffic shaping policy.
        '''
        return self.data['shapingPolicy']

