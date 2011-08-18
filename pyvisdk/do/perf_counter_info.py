# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfCounterInfo(vim, *args, **kwargs):
    '''This data object type contains metadata for a performance counter. See
    PerformanceManager for definitions of available counters.'''
    
    obj = vim.client.factory.create('ns0:PerfCounterInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'associatedCounterId', 'groupInfo', 'key', 'level', 'nameInfo',
        'perDeviceLevel', 'rollupType', 'statsType', 'unitInfo' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    