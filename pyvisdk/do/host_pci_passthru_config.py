
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPciPassthruConfig(DynamicData):
    '''This data object provides information about the state of PciPassthru for all pci
        devices.
    '''
    
    def __init__(self, id, passthruEnabled):
        # MUST define these
        super(HostPciPassthruConfig, self).__init__()
    
        self.data['id'] = id
        self.data['passthruEnabled'] = passthruEnabled
    
    
    @property
    def id(self):
        '''The name ID of this PCI, composed of "bus:slot.function".
        '''
        return self.data['id']

    @property
    def passthruEnabled(self):
        '''Whether passThru is has been configured for this device
        '''
        return self.data['passthruEnabled']

