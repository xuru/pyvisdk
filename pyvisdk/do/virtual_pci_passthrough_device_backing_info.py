
from pyvisdk.do.virtual_device_device_backing_info import VirtualDeviceDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualPCIPassthroughDeviceBackingInfo(VirtualDeviceDeviceBackingInfo):
    '''The VirtualPCIPassthrough.DeviceBackingInfo data object type contains information
        about the backing that maps the virtual device onto a physical device.
    '''
    
    def __init__(self, deviceId, id, systemId, vendorId):
        # MUST define these
        super(VirtualPCIPassthroughDeviceBackingInfo, self).__init__()
    
        self.data['deviceId'] = deviceId
        self.data['id'] = id
        self.data['systemId'] = systemId
        self.data['vendorId'] = vendorId
    
    
    @property
    def deviceId(self):
        '''The device ID of this PCI.
        '''
        return self.data['deviceId']

    @property
    def id(self):
        '''The name ID of this PCI, composed of "bus:slot.function".
        '''
        return self.data['id']

    @property
    def systemId(self):
        '''The ID of the system the PCI device is attached to.
        '''
        return self.data['systemId']

    @property
    def vendorId(self):
        '''The vendor ID for this PCI device.
        '''
        return self.data['vendorId']

