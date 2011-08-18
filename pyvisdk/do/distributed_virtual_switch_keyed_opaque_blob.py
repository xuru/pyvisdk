# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchKeyedOpaqueBlob(vim, *args, **kwargs):
    '''This class defines a data structure to hold opaque binary data identified by a
    key.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchKeyedOpaqueBlob')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'key', 'opaqueData' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    