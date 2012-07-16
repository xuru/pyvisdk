
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineQuickStats(vim, *args, **kwargs):
    '''A set of statistics that are typically updated with near real-time regularity.
    This data object type does not support notification, for scalability reasons.
    Therefore, changes in QuickStats do not generate property collector updates. To
    monitor statistics values, use the statistics and alarms modules instead.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineQuickStats')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'guestHeartbeatStatus' ]
    optional = [ 'balloonedMemory', 'compressedMemory', 'consumedOverheadMemory',
        'distributedCpuEntitlement', 'distributedMemoryEntitlement', 'ftLatencyStatus',
        'ftLogBandwidth', 'ftSecondaryLatency', 'guestMemoryUsage', 'hostMemoryUsage',
        'overallCpuDemand', 'overallCpuUsage', 'privateMemory', 'sharedMemory',
        'ssdSwappedMemory', 'staticCpuEntitlement', 'staticMemoryEntitlement',
        'swappedMemory', 'uptimeSeconds', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    