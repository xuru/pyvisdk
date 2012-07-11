
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionInfo(vim, *args, **kwargs):
    '''Information about the partitions on a disk. A DiskPartitionInfo object provides
    two different views into the partitions on a disk:* A detailed specification
    that is used to create the partition table. * A convenient view that shows the
    allocations of blocks as a contiguous sequence of block ranges.See
    RetrieveDiskPartitionInfoSee ComputeDiskPartitionInfoSee UpdateDiskPartitions'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'deviceName', 'layout', 'spec' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    