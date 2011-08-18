# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualHardware(vim, *args, **kwargs):
    '''The VirtualHardware data object type contains the complete configuration of the
    hardware in a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualHardware')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'device', 'memoryMB', 'numCPU' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    