# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterHostPowerAction(vim, *args, **kwargs):
    '''Describes a single host power action.'''
    
    obj = vim.client.factory.create('ns0:ClusterHostPowerAction')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'target', 'type', 'cpuCapacityMHz', 'memCapacityMB', 'operationType',
        'powerConsumptionWatt' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    