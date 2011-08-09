
from pyvisdk.do.host_virtual_switch_bridge import HostVirtualSwitchBridge
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualSwitchSimpleBridge(HostVirtualSwitchBridge):
    '''A bridge that is statically bound to a single physical network adapter.
    '''
    
    def __init__(self, nicDevice):
        # MUST define these
        super(HostVirtualSwitchSimpleBridge, self).__init__()
    
        self.data['nicDevice'] = nicDevice
    
    
    @property
    def nicDevice(self):
        '''The key of the physical network adapter to be bridged.
        '''
        return self.data['nicDevice']

