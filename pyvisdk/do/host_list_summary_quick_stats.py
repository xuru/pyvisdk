# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostListSummaryQuickStats(vim, *args, **kwargs):
    '''Basic host statistics.Included in the host statistics are fairness scores.
    Fairness scores are represented in units with relative values, meaning they are
    evaluated relative to the scores of other hosts. They should not be thought of
    as having any particular absolute value. Each fairness unit represents an
    increment of 0.001 in a fairness score. The further the fairness score diverges
    from 1, the less fair the allocation. Therefore, a fairness score of 990,
    representing 0.990, is more fair than a fairness score of 1015, which
    represents 1.015. This is because 1.015 is further from 1 than 0.990.'''
    
    obj = vim.client.factory.create('ns0:HostListSummaryQuickStats')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'distributedCpuFairness', 'distributedMemoryFairness', 'overallCpuUsage',
        'overallMemoryUsage', 'uptime' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    