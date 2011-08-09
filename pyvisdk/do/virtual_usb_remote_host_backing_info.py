
from pyvisdk.do.virtual_device_device_backing_info import VirtualDeviceDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualUSBRemoteHostBackingInfo(VirtualDeviceDeviceBackingInfo):
    '''The VirtualUSBRemoteHostBackingInfo data object identifies a host and a USB device
        that is attached to the host. Use this object to configure support for
        persistent access to the USB device when vMotion operations migrate a
        virtual machine to a different host. The vCenter Server will not migrate
        the virtual machine to a host that does not support the USB remote host
        backing capability.Specify remote host backing as part of the USB device
        configuration when you create or reconfigure a virtual machine
        (VirtualMachineConfigSpec.deviceChange.device.backing).To identify the USB
        device, you specify an autoconnect pattern for the deviceName. The virtual
        machine can connect to the USB device if the ESX server can find a USB
        device described by the autoconnect pattern. The autoconnect pattern
        consists of name:value pairs. You can use any combination of the following
        fields.* path - USB connection path on the host * pid - idProduct field in
        the USB device descriptor * vid - idVendor field in the USB device
        descriptor * hostId - unique ID for the host * speed - device speed (low,
        full, or high)For example, the following pattern identifies a USB
        device:????This pattern identifies the USB device connected to port 1/3/0
        on the host with the unique id .Special characters for autoconnect pattern
        values:* The name and value are separated by a colon (:). * Name:value
        pairs are separated by spaces. * The escape character is a backslash (\).
        Use a single backslash to embed a space in a value. Use a double
        blackslash to embed a single backslash in the value.
    '''
    
    def __init__(self, hostname):
        # MUST define these
        super(VirtualUSBRemoteHostBackingInfo, self).__init__()
    
        self.data['hostname'] = hostname
    
    
    @property
    def hostname(self):
        '''Name of the ESX host to which the physical USB device is attached
        (HostSystem.name). When you configure remote host backing, hostname must
        identify the local host on which the virtual machine is running.
        '''
        return self.data['hostname']

