
from pyvisdk.do.dvs_config_info import DVSConfigInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMwareDVSConfigInfo(DVSConfigInfo):
    '''This class defines the VMware specific configuration for DistributedVirtualSwitch.
    '''
    
    def __init__(self, linkDiscoveryProtocolConfig, maxMtu, pvlanConfig):
        # MUST define these
        super(VMwareDVSConfigInfo, self).__init__()
    
        self.data['linkDiscoveryProtocolConfig'] = linkDiscoveryProtocolConfig
        self.data['maxMtu'] = maxMtu
        self.data['pvlanConfig'] = pvlanConfig
    
    
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
    def pvlanConfig(self):
        '''The PVLAN configured in the switch.
        '''
        return self.data['pvlanConfig']

