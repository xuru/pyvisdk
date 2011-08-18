# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSNetworkResourcePoolAllocationInfo(vim, *args, **kwargs):
    '''Resource allocation information for a network resource pool.'''
    
    obj = vim.client.factory.create('ns0:DVSNetworkResourcePoolAllocationInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'limit', 'shares' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    