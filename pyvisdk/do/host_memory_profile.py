# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMemoryProfile(vim, *args, **kwargs):
    '''Memory configuration for the host. This may not be valid all versions of the
    host.'''
    
    obj = vim.client.factory.create('ns0:HostMemoryProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'policy' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    