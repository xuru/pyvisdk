# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchPortCriteria(vim, *args, **kwargs):
    '''The criteria specification for selecting ports.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchPortCriteria')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'active', 'connected', 'inside', 'portgroupKey', 'portKey', 'scope',
        'uplinkPort' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    