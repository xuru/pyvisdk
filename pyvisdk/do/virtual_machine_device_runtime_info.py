# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineDeviceRuntimeInfo(vim, *args, **kwargs):
    '''The DeviceRuntimeInfo data object type provides information about the execution
    state of a single virtual device.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineDeviceRuntimeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'key', 'runtimeState' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    