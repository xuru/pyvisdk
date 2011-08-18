# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'balloonedMemory', 'compressedMemory', 'consumedOverheadMemory',
        'distributedCpuEntitlement', 'distributedMemoryEntitlement',
        'guestMemoryUsage', 'hostMemoryUsage', 'overallCpuDemand', 'overallCpuUsage',
        'overheadMemory', 'privateMemory', 'sharedMemory', 'staticCpuEntitlement',
        'staticMemoryEntitlement', 'swappedMemory' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    