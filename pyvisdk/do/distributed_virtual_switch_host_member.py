# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchHostMember(vim, *args, **kwargs):
    '''The data object that represents a host member in the distributed virtual
    switch.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchHostMember')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'config', 'productInfo', 'status', 'statusDetail', 'uplinkPortKey' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    