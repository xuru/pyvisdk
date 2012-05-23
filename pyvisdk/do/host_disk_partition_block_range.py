
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionBlockRange(vim, *args, **kwargs):
    '''A BlockRange data object type describes a contiguous set of blocks on a disk. A
    BlockRange may describe either a partition or unpartitioned (primordial) blocks
    on the disk.'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionBlockRange')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'end', 'start', 'type' ]
    optional = [ 'partition', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    