# -*- coding: ascii -*-

import logging

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
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'balloonedMemory', 'compressedMemory', 'consumedOverheadMemory',
        'distributedCpuEntitlement', 'distributedMemoryEntitlement', 'ftLatencyStatus',
        'ftLogBandwidth', 'ftSecondaryLatency', 'guestHeartbeatStatus',
        'guestMemoryUsage', 'hostMemoryUsage', 'overallCpuDemand', 'overallCpuUsage',
        'privateMemory', 'sharedMemory', 'staticCpuEntitlement',
        'staticMemoryEntitlement', 'swappedMemory', 'uptimeSeconds' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    