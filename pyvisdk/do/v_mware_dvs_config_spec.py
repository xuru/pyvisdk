
from pyvisdk.do.dvs_config_spec import DVSConfigSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMwareDVSConfigSpec(DVSConfigSpec):
    '''This class defines the VMware specific configuration for DistributedVirtualSwitch.
    '''
    
    def __init__(self, linkDiscoveryProtocolConfig, maxMtu, pvlanConfigSpec):
        # MUST define these
        super(VMwareDVSConfigSpec, self).__init__()
    
        self.data['linkDiscoveryProtocolConfig'] = linkDiscoveryProtocolConfig
        self.data['maxMtu'] = maxMtu
        self.data['pvlanConfigSpec'] = pvlanConfigSpec
    
    
    @property
    def linkDiscoveryProtocolConfig(self):
        '''See LinkDiscoveryProtocolConfig.
        '''
        return self.data['linkDiscoveryProtocolConfig']

    @property
    def maxMtu(self):
        '''The maximum MTU in the switch.
        '''
        return self.data['maxMtu']

    @property
    def pvlanConfigSpec(self):
        '''The PVLAN configuration specification.
        '''
        return self.data['pvlanConfigSpec']

