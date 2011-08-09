
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDevice(DynamicData):
    '''VirtualDevice is the base data object type for devices in a virtual machine. This
        type contains enough information about a virtual device to allow clients
        to display devices they do not recognize. For example, a client with an
        older version than the server to which it connects may see a device
        without knowing what it is.
    '''
    
    def __init__(self, backing, connectable, controllerKey, deviceInfo, key, unitNumber):
        # MUST define these
        super(VirtualDevice, self).__init__()
    
        self.data['backing'] = backing
        self.data['connectable'] = connectable
        self.data['controllerKey'] = controllerKey
        self.data['deviceInfo'] = deviceInfo
        self.data['key'] = key
        self.data['unitNumber'] = unitNumber
    
    
    @property
    def backing(self):
        '''Information about the backing of this virtual device presented in the context of
        the virtual machine's environment. Not all devices are required to have
        backing information.
        '''
        return self.data['backing']

    @property
    def connectable(self):
        '''Provides information about restrictions on removing this device while a virtual
        machine is running. If the device is not removable, then this property is
        null.
        '''
        return self.data['connectable']

    @property
    def controllerKey(self):
        '''Object key for the controller object for this device. This property contains the
        key property value of the controller device object.
        '''
        return self.data['controllerKey']

    @property
    def deviceInfo(self):
        '''Provides a label and summary information for the device.
        '''
        return self.data['deviceInfo']

    @property
    def key(self):
        '''A unique key that distinguishes this device from other devices in the same virtual
        machine. Keys are immutable but may be recycled; that is, a key does not
        change as long as the device is associated with a particular virtual
        machine. However, once a device is removed, its key may be used when
        another device is added.
        '''
        return self.data['key']

    @property
    def unitNumber(self):
        '''The unit number of this device on its controller. This property is null if the
        controller property is null (for example, when the device is not attached
        to a specific controller object).
        '''
        return self.data['unitNumber']

