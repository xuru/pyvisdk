
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionAttributes(vim, *args, **kwargs):
    '''Information about a single disk partition. A partition is a contiguous set of
    blocks on a disk that is marked for use. The typeId identifies the purpose of
    the data in the partition.'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionAttributes')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'attributes', 'endSector', 'logical', 'partition', 'startSector', 'type' ]
    optional = [ 'guid', 'partitionAlignment', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    