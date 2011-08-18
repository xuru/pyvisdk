# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchHostProductSpec(vim, *args, **kwargs):
    '''This data object type is a subset of AboutInfo. An object of this type can be
    used to describe the specification for a host.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchHostProductSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'productLineId', 'version' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    