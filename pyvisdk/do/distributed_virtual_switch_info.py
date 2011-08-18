# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchInfo(vim, *args, **kwargs):
    '''This class describes a DistributedVirtualSwitch that a device backing can
    attached to its ports.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'distributedVirtualSwitch', 'switchName', 'switchUuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    