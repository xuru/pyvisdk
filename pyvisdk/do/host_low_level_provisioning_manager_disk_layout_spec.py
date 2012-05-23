
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostLowLevelProvisioningManagerDiskLayoutSpec(vim, *args, **kwargs):
    '''File layout spec of a virtual disk. The disk could be either a base-disk or a
    delta disk.'''
    
    obj = vim.client.factory.create('ns0:HostLowLevelProvisioningManagerDiskLayoutSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'busNumber', 'controllerType', 'dstFilename', 'srcFilename', 'unitNumber' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    