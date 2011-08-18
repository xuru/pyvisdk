# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSNetworkResourcePoolConfigSpec(vim, *args, **kwargs):
    '''The configuration specification data object to update the resource
    configuration for a network resource pool.'''
    
    obj = vim.client.factory.create('ns0:DVSNetworkResourcePoolConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'allocationInfo', 'configVersion', 'key' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    