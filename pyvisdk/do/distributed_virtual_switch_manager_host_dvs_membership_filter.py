# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchManagerHostDvsMembershipFilter(vim, *args, **kwargs):
    '''Check host compatibility against all hosts in the DVS (or not in the DVS if
    inclusive flag in base class is false)'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchManagerHostDvsMembershipFilter')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'inclusive', 'distributedVirtualSwitch' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    