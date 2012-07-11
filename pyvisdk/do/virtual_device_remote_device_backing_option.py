
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceRemoteDeviceBackingOption(vim, *args, **kwargs):
    '''VirtualDeviceOption.RemoteDeviceBackingOption describes the options for a
    remote device backing. The primary difference between a remote device backing
    and a local device backing is that the VirtualCenter server cannot provide a
    list of remote host devices available for this virtual device backing.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceRemoteDeviceBackingOption')

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
    