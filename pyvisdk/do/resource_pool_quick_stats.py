
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourcePoolQuickStats(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:ResourcePoolQuickStats')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'balloonedMemory', 'compressedMemory', 'consumedOverheadMemory',
        'distributedCpuEntitlement', 'distributedMemoryEntitlement',
        'guestMemoryUsage', 'hostMemoryUsage', 'overallCpuDemand', 'overallCpuUsage',
        'overheadMemory', 'privateMemory', 'sharedMemory', 'staticCpuEntitlement',
        'staticMemoryEntitlement', 'swappedMemory' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    