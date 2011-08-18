# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfMetricSeries(vim, *args, **kwargs):
    '''This is a generic data object type that stores values for a specific
    performance metric. Useful data objects that store actual metric values extend
    this data object (see PerfMetricIntSeries).'''
    
    obj = vim.client.factory.create('ns0:PerfMetricSeries')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'id' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    