
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualUSBUSBBackingOption(vim, *args, **kwargs):
    '''The VirtualUSBUSBBackingOption data object contains the options for virtual
    backing for a USB device. This backing option indicates support for a local
    connection where the virtual machine will remain on the host to which the USB
    device is attached.'''
    
    obj = vim.client.factory.create('ns0:VirtualUSBUSBBackingOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'autoDetectAvailable', 'type' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    