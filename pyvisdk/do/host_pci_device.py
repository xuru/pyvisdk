
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPciDevice(DynamicData):
    '''This data object type describes information about a single Peripheral Component
        Interconnect (PCI) device.
    '''
    
    def __init__(self, bus, classId, deviceId, deviceName, function, id, parentBridge, slot, subDeviceId, subVendorId, vendorId, vendorName):
        # MUST define these
        super(HostPciDevice, self).__init__()
    
        self.data['bus'] = bus
        self.data['classId'] = classId
        self.data['deviceId'] = deviceId
        self.data['deviceName'] = deviceName
        self.data['function'] = function
        self.data['id'] = id
        self.data['parentBridge'] = parentBridge
        self.data['slot'] = slot
        self.data['subDeviceId'] = subDeviceId
        self.data['subVendorId'] = subVendorId
        self.data['vendorId'] = vendorId
        self.data['vendorName'] = vendorName
    
    
    @property
    def bus(self):
        '''The bus ID of this PCI.
        '''
        return self.data['bus']

    @property
    def classId(self):
        '''The class of this PCI.
        '''
        return self.data['classId']

    @property
    def deviceId(self):
        '''The device ID of this PCI.
        '''
        return self.data['deviceId']

    @property
    def deviceName(self):
        '''The device name of this PCI.
        '''
        return self.data['deviceName']

    @property
    def function(self):
        '''The function ID of this PCI.
        '''
        return self.data['function']

    @property
    def id(self):
        '''The name ID of this PCI, composed of "bus:slot.function".
        '''
        return self.data['id']

    @property
    def parentBridge(self):
        '''The parent bridge of this PCI.
        '''
        return self.data['parentBridge']

    @property
    def slot(self):
        '''The slot ID of this PCI.
        '''
        return self.data['slot']

    @property
    def subDeviceId(self):
        '''The subdevice ID of this PCI.
        '''
        return self.data['subDeviceId']

    @property
    def subVendorId(self):
        '''The subvendor ID of this PCI.
        '''
        return self.data['subVendorId']

    @property
    def vendorId(self):
        '''The vendor ID of this PCI.
        '''
        return self.data['vendorId']

    @property
    def vendorName(self):
        '''The vendor name of this PCI.
        '''
        return self.data['vendorName']

