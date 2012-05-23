
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourcePoolQuickStats(vim, *args, **kwargs):
    '''A set of statistics that are typically updated with near real-time regularity.
    These statistics are aggregates of the corresponding statistics of all virtual
    machines in the given resource pool, and unless otherwise noted, only make
    sense when at least one virtual machine in the given resource pool is powered
    on. This data object type does not support notification, for scalability
    reasons. Therefore, changes in QuickStats do not generate property collector
    updates. To monitor statistics values, use the statistics and alarms modules
    instead.'''
    
    obj = vim.client.factory.create('ns0:ResourcePoolQuickStats')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'balloonedMemory', 'compressedMemory', 'consumedOverheadMemory',
        'distributedCpuEntitlement', 'distributedMemoryEntitlement',
        'guestMemoryUsage', 'hostMemoryUsage', 'overallCpuDemand', 'overallCpuUsage',
        'overheadMemory', 'privateMemory', 'sharedMemory', 'staticCpuEntitlement',
        'staticMemoryEntitlement', 'swappedMemory', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    