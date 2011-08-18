# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchManagerHostContainer(vim, *args, **kwargs):
    '''Check host compatibility for all hosts in the container. If the recursive flag
    is true, then check hosts at all levels within this container, otherwise check
    only at the container level. In case of container being a Datacenter, the
    recursive flag is applied to its HostFolder.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchManagerHostContainer')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'container', 'recursive' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    