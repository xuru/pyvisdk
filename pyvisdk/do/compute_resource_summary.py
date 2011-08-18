# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ComputeResourceSummary(vim, *args, **kwargs):
    '''This data object type encapsulates a typical set of ComputeResource information
    that is useful for list views and summary pages.'''
    
    obj = vim.client.factory.create('ns0:ComputeResourceSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'effectiveCpu', 'effectiveMemory', 'numCpuCores', 'numCpuThreads',
        'numEffectiveHosts', 'numHosts', 'overallStatus', 'totalCpu', 'totalMemory' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    