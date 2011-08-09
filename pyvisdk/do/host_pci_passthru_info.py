
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPciPassthruInfo(DynamicData):
    '''This data object provides information about the state of PciPassthru for all pci
        devices.
    '''
    
    def __init__(self, dependentDevice, id, passthruActive, passthruCapable, passthruEnabled):
        # MUST define these
        super(HostPciPassthruInfo, self).__init__()
    
        self.data['dependentDevice'] = dependentDevice
        self.data['id'] = id
        self.data['passthruActive'] = passthruActive
        self.data['passthruCapable'] = passthruCapable
        self.data['passthruEnabled'] = passthruEnabled
    
    
    @property
    def dependentDevice(self):
        '''Device which needs to be unclaimed by vmkernel (may be bridge)
        '''
        return self.data['dependentDevice']

    @property
    def id(self):
        '''The name ID of this PCI, composed of "bus:slot.function".
        '''
        return self.data['id']

    @property
    def passthruActive(self):
        '''Whether passThru is active for this device (meaning enabled + rebooted)
        '''
        return self.data['passthruActive']

    @property
    def passthruCapable(self):
        '''Whether passThru is even possible for this device (decided by vmkctl)
        '''
        return self.data['passthruCapable']

    @property
    def passthruEnabled(self):
        '''Whether passThru has been configured by the user
        '''
        return self.data['passthruEnabled']

