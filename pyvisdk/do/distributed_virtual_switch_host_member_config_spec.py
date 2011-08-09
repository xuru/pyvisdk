
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchHostMemberConfigSpec(DynamicData):
    '''Specification to reconfigure a HostMember.
    '''
    
    def __init__(self, backing, host, maxProxySwitchPorts, operation, vendorSpecificConfig):
        # MUST define these
        super(DistributedVirtualSwitchHostMemberConfigSpec, self).__init__()
    
        self.data['backing'] = backing
        self.data['host'] = host
        self.data['maxProxySwitchPorts'] = maxProxySwitchPorts
        self.data['operation'] = operation
        self.data['vendorSpecificConfig'] = vendorSpecificConfig
    
    
    @property
    def backing(self):
        '''Indicating whether to select individual physical NICs or an existing vSwitch.
        '''
        return self.data['backing']

    @property
    def host(self):
        '''The host to join the DistributedVirtualSwitch in creating a HostMember or identify
        the existing HostMember to be reconfigured.
        '''
        return self.data['host']

    @property
    def maxProxySwitchPorts(self):
        '''The maximum number of ports allowed to be created in the proxy switch.
        '''
        return self.data['maxProxySwitchPorts']

    @property
    def operation(self):
        '''The host member operation type. See ConfigSpecOperation for valid values.
        '''
        return self.data['operation']

    @property
    def vendorSpecificConfig(self):
        '''An opaque binary blob that stores vendor specific configuration.
        '''
        return self.data['vendorSpecificConfig']

