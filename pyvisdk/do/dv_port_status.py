
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortStatus(DynamicData):
    '''The runtime information of a DistributedVirtualPort.
    '''
    
    def __init__(self, blocked, linkPeer, linkUp, macAddress, mtu, statusDetail, trunkingMode, vlanIds, vmDirectPathGen2Active, vmDirectPathGen2InactiveReasonExtended, vmDirectPathGen2InactiveReasonNetwork, vmDirectPathGen2InactiveReasonOther):
        # MUST define these
        super(DVPortStatus, self).__init__()
    
        self.data['blocked'] = blocked
        self.data['linkPeer'] = linkPeer
        self.data['linkUp'] = linkUp
        self.data['macAddress'] = macAddress
        self.data['mtu'] = mtu
        self.data['statusDetail'] = statusDetail
        self.data['trunkingMode'] = trunkingMode
        self.data['vlanIds'] = vlanIds
        self.data['vmDirectPathGen2Active'] = vmDirectPathGen2Active
        self.data['vmDirectPathGen2InactiveReasonExtended'] = vmDirectPathGen2InactiveReasonExtended
        self.data['vmDirectPathGen2InactiveReasonNetwork'] = vmDirectPathGen2InactiveReasonNetwork
        self.data['vmDirectPathGen2InactiveReasonOther'] = vmDirectPathGen2InactiveReasonOther
    
    
    @property
    def blocked(self):
        '''Whether the port is blocked by switch implementation.
        '''
        return self.data['blocked']

    @property
    def linkPeer(self):
        '''The name of the connected entity.
        '''
        return self.data['linkPeer']

    @property
    def linkUp(self):
        '''Whether the port is in linkUp status.
        '''
        return self.data['linkUp']

    @property
    def macAddress(self):
        '''The MAC address that is used at this port.
        '''
        return self.data['macAddress']

    @property
    def mtu(self):
        '''The MTU of the port. Currently, this property can be set only at the switch level.
        Attempting to change it at the portgroup or port level raises an
        exception.
        '''
        return self.data['mtu']

    @property
    def statusDetail(self):
        '''Additional information regarding the port's current status.
        '''
        return self.data['statusDetail']

    @property
    def trunkingMode(self):
        '''True if the port VLAN tagging/stripping is disabled.
        '''
        return self.data['trunkingMode']

    @property
    def vlanIds(self):
        '''The VLAN ID of the port.
        '''
        return self.data['vlanIds']

    @property
    def vmDirectPathGen2Active(self):
        '''Flag to indicate whether VMDirectPath Gen 2 is active on this port. If false, the
        reason(s) for inactivity will be provided in one or more of
        vmDirectPathGen2InactiveReasonNetwork,
        vmDirectPathGen2InactiveReasonOther, and
        vmDirectPathGen2InactiveReasonExtended.
        '''
        return self.data['vmDirectPathGen2Active']

    @property
    def vmDirectPathGen2InactiveReasonExtended(self):
        '''If vmDirectPathGen2Active is false, this property may contain an explanation
        provided by the platform, beyond the reasons (if any) enumerated in
        vmDirectPathGen2InactiveReasonNetwork and/or
        vmDirectPathGen2InactiveReasonOther.
        '''
        return self.data['vmDirectPathGen2InactiveReasonExtended']

    @property
    def vmDirectPathGen2InactiveReasonNetwork(self):
        '''If vmDirectPathGen2Active is false, this array will be populated with reasons for
        the inactivity that are related to network state or configuration (chosen
        from VmDirectPathGen2InactiveReasonNetwork). Other reasons for inactivity
        will be provided in vmDirectPathGen2InactiveReasonOther. If there is a
        reason for inactivity that cannot be described by the available constants,
        vmDirectPathGen2InactiveReasonExtended will be populated with an
        additional explanation provided by the platform.
        '''
        return self.data['vmDirectPathGen2InactiveReasonNetwork']

    @property
    def vmDirectPathGen2InactiveReasonOther(self):
        '''If vmDirectPathGen2Active is false, this array will be populated with reasons for
        the inactivity that are not related to network state or configuration
        (chosen from VmDirectPathGen2InactiveReasonOther). Network-related reasons
        for inactivity will be provided in vmDirectPathGen2InactiveReasonNetwork.
        If there is a reason for inactivity that cannot be described by the
        available constants, vmDirectPathGen2InactiveReasonExtended will be
        populated with an additional explanation provided by the platform.
        '''
        return self.data['vmDirectPathGen2InactiveReasonOther']

