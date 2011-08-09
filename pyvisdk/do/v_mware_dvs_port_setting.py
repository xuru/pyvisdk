
from pyvisdk.do.dv_port_setting import DVPortSetting
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMwareDVSPortSetting(DVPortSetting):
    '''This class defines the VMware specific configuration for DistributedVirtualPort.
    '''
    
    def __init__(self, qosTag, securityPolicy, txUplink, uplinkTeamingPolicy, vlan):
        # MUST define these
        super(VMwareDVSPortSetting, self).__init__()
    
        self.data['qosTag'] = qosTag
        self.data['securityPolicy'] = securityPolicy
        self.data['txUplink'] = txUplink
        self.data['uplinkTeamingPolicy'] = uplinkTeamingPolicy
        self.data['vlan'] = vlan
    
    
    @property
    def qosTag(self):
        '''This property is currently not supported.
        '''
        return self.data['qosTag']

    @property
    def securityPolicy(self):
        '''The security policy.
        '''
        return self.data['securityPolicy']

    @property
    def txUplink(self):
        '''Whether this should forward all incoming traffic out an uplink
        '''
        return self.data['txUplink']

    @property
    def uplinkTeamingPolicy(self):
        '''The uplink teaming policy. This property is ignored for uplink ports.
        '''
        return self.data['uplinkTeamingPolicy']

    @property
    def vlan(self):
        '''The VLAN Specification of the port.
        '''
        return self.data['vlan']

