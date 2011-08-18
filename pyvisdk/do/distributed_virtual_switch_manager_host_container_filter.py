# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchManagerHostContainerFilter(vim, *args, **kwargs):
    '''Check host compatibility against all hosts in this
    DistributedVirtualSwitchManagerHostContainer'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchManagerHostContainerFilter')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'inclusive', 'hostContainer' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    