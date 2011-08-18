# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualUSBOption(vim, *args, **kwargs):
    '''The VirtualUSBOption data object type contains options for USB device
    configuration on a virtual machine. The vSphere API supports the following
    options:* Local host USB connection (VirtualUSBUSBBackingOption) * Remote host
    USB connection (VirtualUSBRemoteHostBackingOption)For information about USB
    device configuration, see VirtualUSB.'''
    
    obj = vim.client.factory.create('ns0:VirtualUSBOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    