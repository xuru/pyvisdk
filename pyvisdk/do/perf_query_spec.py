# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfQuerySpec(vim, *args, **kwargs):
    '''This data object specifies the query parameters, including the managed object
    reference to the target entity for statistics retrieval.* If the optional
    intervalId is omitted, the metrics are returned in their originally sampled
    interval. * When an intervalId is specified, the server tries to summarize the
    information for the specified intervalId. However, if that interval does not
    exist or has no data, the server summarizes the information using the best
    interval available. * If the range between startTime and endTime crosses
    multiple sample interval periods, the result contains data from the longest
    interval in the period.'''
    
    obj = vim.client.factory.create('ns0:PerfQuerySpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'endTime', 'entity', 'format', 'intervalId', 'maxSample', 'metricId',
        'startTime' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    