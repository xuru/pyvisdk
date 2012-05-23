
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualUSBOption(vim, *args, **kwargs):
    '''The VirtualUSBOption data object type contains options for USB device
    configuration on a virtual machine. The vSphere API supports the following
    options:* Local host USB connection (VirtualUSBUSBBackingOption) * Remote host
    USB connection (VirtualUSBRemoteHostBackingOption)For information about USB
    device configuration, see VirtualUSB.'''
    
    obj = vim.client.factory.create('ns0:VirtualUSBOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'deprecated', 'hotRemoveSupported', 'plugAndPlay', 'type' ]
    optional = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'licensingLimit', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    