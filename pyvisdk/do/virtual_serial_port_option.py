# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSerialPortOption(vim, *args, **kwargs):
    '''The data object contains the options for configuring the virtual serial port
    device defined by the data object. These options include information about how
    the device is backed physically on the host: by a network socket, a host file,
    a host serial port device, or a pipe to another process.'''
    
    obj = vim.client.factory.create('ns0:VirtualSerialPortOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type', 'yieldOnPoll' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    