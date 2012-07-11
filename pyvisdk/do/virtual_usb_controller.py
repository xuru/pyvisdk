
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualUSBController(vim, *args, **kwargs):
    '''The VirtualUSBController data object describes a virtual USB controller and
    contains a list of the devices connected to the controller. A virtual machine
    must have a virtual USB controller before you can add a USB device to the
    virtual machine configuration. To add a controller, include a
    VirtualUSBController object in the VirtualDeviceConfigSpec for your virtual
    machine configuration. You can add only one controller to a virtual machine. A
    virtual USB controller supports up to 20 USB device connections on the virtual
    machine.The ESX Server host must have the USB controller hardware and modules
    that support USB 2.0 and USB1.1. You can use a maximum of 15 USB controllers on
    a host. If your system includes an additional number of controllers with
    connected devices, the additional devices will not be available to virtual
    machines on the host.You must remove all USB devices from a virtual machine
    before you can remove the USB controller.'''
    
    obj = vim.client.factory.create('ns0:VirtualUSBController')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'busNumber', 'key' ]
    optional = [ 'autoConnectDevices', 'ehciEnabled', 'device', 'backing', 'connectable',
        'controllerKey', 'deviceInfo', 'unitNumber', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    