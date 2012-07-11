
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualUSBRemoteHostBackingOption(vim, *args, **kwargs):
    '''The VirtualUSBRemoteHostBackingOption data object contains options for remote
    host USB configuration. This backing option indicates support for persistent
    USB connections when vMotion operations migrate virtual machines to different
    hosts.'''
    
    obj = vim.client.factory.create('ns0:VirtualUSBRemoteHostBackingOption')

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
    