
from pyvisdk.do.virtual_device import VirtualDevice
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualUSB(VirtualDevice):
    '''The VirtualUSB data object describes the USB device configuration for a virtual
        machine. You can attach a USB device to an ESX host. The device is
        available to only one virtual machine at a time. When you remove the
        device from the virtual machine, it becomes available to other virtual
        machines located on the host. You can add up to 20 USB devices to a
        virtual machine. Virtual USB support requires virtual machine hardware
        version 7 or later.The VirtualUSB object represents either a configuration
        to be applied to the virtual machine or the current device configuration
        on the virtual machine.* To configure a USB connection for the virtual
        machine, add a VirtualUSB object to the VirtualDeviceConfigSpec. Use USB
        backing (VirtualUSBUSBBackingInfo) to establish a connection with a
        virtual machine that will remain on the host to which the USB device is
        attached. The vSphere Server does not support vMotion for standard USB
        backing. To configure vMotion support for a virtual machine with a USB
        connection, use remote host backing for the USB connection
        (VirtualUSBRemoteHostBackingInfo).To configure a USB device for a virtual
        machine, the virtual machine must have a USB controller. To add a
        controller, include a VirtualUSBController object in the virtual device
        specification for your virtual machine configuration. You can add only one
        USB controller to a virtual machine.* To determine USB device
        configuration status for the virtual machine, check the virtual hardware
        device list (VirtualHardware.device). The presence of the VirtualUSB
        object in the hardware device list indicates that the virtual machine is
        configured to use a USB device. The connected property indicates whether
        the virtual machine is connected to the device.To determine the USB
        options available on the host, use the QueryConfigOption method to
        retrieve the virtual machine configuration. The presence of the
        VirtualUSBOption object in the retrieved configuration
        (VirtualMachineConfigOption.hardwareOptions.virtualDeviceOption) indicates
        that the host supports USB connections.The following operations will
        disconnect a USB device, losing data if data transfer is in progress over
        the USB connection.* Hot add of memory, CPU, or PCI devices. A hot add
        operation disconnects only USB devices for virtual machines that use a
        local connection to the device (VirtualUSBUSBBackingInfo). * Suspend and
        resume on a virtual machine. * vMotion of a virtual machine with a USB
        connection, if you are not using remote host USB backing.The following
        services do not support USB connections.* Fault Tolerance virtual machines
        cannot use USB devices. * DPM (Distributed Power Management) will put a
        host into standby, regardless of any connections to USB devices on the
        host. * DRS (Distributed Resource Scheduling) may power-off hosts that
        have USB connections to virtual machines.
    '''
    
    def __init__(self, connected, family, product, speed, vendor):
        # MUST define these
        super(VirtualUSB, self).__init__()
    
        self.data['connected'] = connected
        self.data['family'] = family
        self.data['product'] = product
        self.data['speed'] = speed
        self.data['vendor'] = vendor
    
    
    @property
    def connected(self):
        '''Flag indicating whether the device is currently connected. The virtual machine is
        not connected to the device if the autoconnect pattern specified in the
        USB device backing (VirtualDeviceDeviceBackingInfo.deviceName) can not be
        satisfied, either because there is no such device, or the matching device
        is not available. Valid only while the virtual machine is running.
        '''
        return self.data['connected']

    @property
    def family(self):
        '''Device class families. For possible values see VirtualMachineUsbInfoFamily.
        '''
        return self.data['family']

    @property
    def product(self):
        '''Product ID of the USB device.
        '''
        return self.data['product']

    @property
    def speed(self):
        '''Device speeds detected by server. For possible values see
        VirtualMachineUsbInfoSpeed.
        '''
        return self.data['speed']

    @property
    def vendor(self):
        '''Vendor ID of the USB device.
        '''
        return self.data['vendor']

