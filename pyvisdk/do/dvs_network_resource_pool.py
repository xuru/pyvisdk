# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSNetworkResourcePool(vim, *args, **kwargs):
    '''DataObject describing the resource configuration and management of network
    resource pools.'''
    
    obj = vim.client.factory.create('ns0:DVSNetworkResourcePool')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'allocationInfo', 'configVersion', 'description', 'key', 'name' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    