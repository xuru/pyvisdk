
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineRelocateSpecDiskLocator(vim, *args, **kwargs):
    '''The DiskLocator data object type specifies a virtual disk device (by ID) and a
    datastore locator for the disk's storage.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineRelocateSpecDiskLocator')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'datastore', 'diskId' ]
    optional = [ 'diskBackingInfo', 'diskMoveType', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    