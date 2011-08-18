# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSerialPortPipeBackingOption(vim, *args, **kwargs):
    '''The data object contains the options for backing a serial port device with a
    pipe to another process.'''
    
    obj = vim.client.factory.create('ns0:VirtualSerialPortPipeBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'endpoint', 'noRxLoss' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    