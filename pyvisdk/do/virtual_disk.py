
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDisk(vim, *args, **kwargs):
    '''This data object type contains information about a disk in a virtual
    machine.The virtual disk backing object types describe the different virtual
    disk backings available. The disk format version in each case describes the
    version of the format that is used.Supported virtual disk backings:'''
    
    obj = vim.client.factory.create('ns0:VirtualDisk')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'capacityInKB', 'key' ]
    optional = [ 'shares', 'storageIOAllocation', 'backing', 'connectable', 'controllerKey',
        'deviceInfo', 'unitNumber', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    