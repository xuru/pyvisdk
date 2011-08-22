
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionLayout(vim, *args, **kwargs):
    '''This data object type describes the disk partition layout specified as a list
    of ordered BlockRanges. This view of the disk partitions shows the data on the
    disk as a contiguous set of BlockRanges.'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionLayout')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'partition' ]
    inherited = [ 'total' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    