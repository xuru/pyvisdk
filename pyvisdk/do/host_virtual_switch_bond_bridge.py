
from pyvisdk.do.host_virtual_switch_bridge import HostVirtualSwitchBridge
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualSwitchBondBridge(HostVirtualSwitchBridge):
    '''This data object type describes a bridge that provides network adapter teaming
        capabilities.
    '''
    
    def __init__(self, beacon, linkDiscoveryProtocolConfig, nicDevice):
        # MUST define these
        super(HostVirtualSwitchBondBridge, self).__init__()
    
        self.data['beacon'] = beacon
        self.data['linkDiscoveryProtocolConfig'] = linkDiscoveryProtocolConfig
        self.data['nicDevice'] = nicDevice
    
    
    @property
    def beacon(self):
        '''The beacon configuration to probe for the validity of a link. If this is set,
        beacon probing is configured and will be used. If this is not set, beacon
        probing is disabled.
        '''
        return self.data['beacon']

    @property
    def linkDiscoveryProtocolConfig(self):
        '''The link discovery protocol configuration for the virtual switch.
        '''
        return self.data['linkDiscoveryProtocolConfig']

    @property
    def nicDevice(self):
        '''The list of keys of the physical network adapters to be bridged.
        '''
        return self.data['nicDevice']

