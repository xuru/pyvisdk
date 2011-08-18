# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterComputeResourceSummary(vim, *args, **kwargs):
    '''The ClusterComputeResourceSummary data object encapsulates runtime properties
    of a ClusterComputeResource.'''
    
    obj = vim.client.factory.create('ns0:ClusterComputeResourceSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'effectiveCpu', 'effectiveMemory', 'numCpuCores', 'numCpuThreads',
        'numEffectiveHosts', 'numHosts', 'overallStatus', 'totalCpu', 'totalMemory',
        'admissionControlInfo', 'currentBalance', 'currentEVCModeKey',
        'currentFailoverLevel', 'numVmotions', 'targetBalance' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    