
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchHostMemberConfigInfo(DynamicData):
    '''Configuration of a HostMember.
    '''
    
    def __init__(self, backing, host, maxProxySwitchPorts, vendorSpecificConfig):
        # MUST define these
        super(DistributedVirtualSwitchHostMemberConfigInfo, self).__init__()
    
        self.data['backing'] = backing
        self.data['host'] = host
        self.data['maxProxySwitchPorts'] = maxProxySwitchPorts
        self.data['vendorSpecificConfig'] = vendorSpecificConfig
    
    
    @property
    def backing(self):
        '''The backing used by the HostMember.
        '''
        return self.data['backing']

    @property
    def host(self):
        '''The host. This property should always be set unless the user's setting does not
        have System.Read privilege on the object referred to by this property.
        '''
        return self.data['host']

    @property
    def maxProxySwitchPorts(self):
        '''The maximum number of ports allowed to be created in the proxy switch.
        '''
        return self.data['maxProxySwitchPorts']

    @property
    def vendorSpecificConfig(self):
        '''An opaque binary blob that stores vendor specific configuration.
        '''
        return self.data['vendorSpecificConfig']

