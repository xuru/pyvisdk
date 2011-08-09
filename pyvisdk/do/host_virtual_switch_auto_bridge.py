
from pyvisdk.do.host_virtual_switch_bridge import HostVirtualSwitchBridge
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualSwitchAutoBridge(HostVirtualSwitchBridge):
    '''This data type describes a bridge that automatically selects a particular physical
        network adapter on the host according to some predetermined policy. Used
        primarily to support mobility scenarios.
    '''
    
    def __init__(self, excludedNicDevice):
        # MUST define these
        super(HostVirtualSwitchAutoBridge, self).__init__()
    
        self.data['excludedNicDevice'] = excludedNicDevice
    
    
    @property
    def excludedNicDevice(self):
        '''List of physical network adapters that have been excluded from participating in
        the AutoBridge
        '''
        return self.data['excludedNicDevice']

