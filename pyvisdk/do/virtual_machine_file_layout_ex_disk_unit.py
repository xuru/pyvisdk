
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineFileLayoutExDiskUnit(vim, *args, **kwargs):
    '''Information about a single unit of a virtual disk, such as the base-disk or a
    delta-disk.A disk-unit consists of at least one descriptor file, and zero or
    more extent files.Sometimes, a disk-unit is also referred to as a .'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineFileLayoutExDiskUnit')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'fileKey' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    