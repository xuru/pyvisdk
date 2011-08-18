# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfMetricId(vim, *args, **kwargs):
    '''This data object type contains information that associates a performance
    counter with a performance metric. When constructing this data object for the
    metricId property of the PerfQuerySpec to submit to one of the
    PerformanceManager query operations, the instance property supports these
    special characters:* An asterisk (*) to specify all instances of the metric for
    the specified counterId * Double-quotes ("") to specify aggregated statistics'''
    
    obj = vim.client.factory.create('ns0:PerfMetricId')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'counterId', 'instance' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    