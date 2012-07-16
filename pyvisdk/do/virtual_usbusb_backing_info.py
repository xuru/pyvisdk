
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualUSBUSBBackingInfo(vim, *args, **kwargs):
    '''The VirtualUSBUSBBackingInfo data object identifies a USB device on the host
    where the virtual machine is located. This type of backing supports only a
    local connection where the virtual machine will remain on the host to which the
    USB device is attached.To identify the USB device, you specify an autoconnect
    pattern for the deviceName. The virtual machine can connect to the USB device
    if the ESX server can find a USB device described by the autoconnect pattern.
    The autoconnect pattern consists of name:value pairs. You can use any
    combination of the following fields.* path - USB connection path on the host *
    pid - idProduct field in the USB device descriptor * vid - idVendor field in
    the USB device descriptor * hostId - unique ID for the host * speed - device
    speed (low, full, or high)For example, the following pattern identifies a USB
    device:This pattern identifies the USB device connected to port 1/3/0 on the
    host with the unique id .Special characters for autoconnect pattern values:*
    The name and value are separated by a colon (:). * Name:value pairs are
    separated by spaces. * The escape character is a backslash (\). Use a single
    backslash to embed a space in a value. Use a double blackslash to embed a
    single backslash in the value.'''
    
    obj = vim.client.factory.create('ns0:VirtualUSBUSBBackingInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'deviceName' ]
    optional = [ 'useAutoDetect', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    