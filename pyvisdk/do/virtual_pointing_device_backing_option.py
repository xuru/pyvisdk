# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPointingDeviceBackingOption(vim, *args, **kwargs):
    '''The DeviceBackingOption data object type represents the options for a pointing
    device backing a VirtualPointingDevice data object type.'''
    
    obj = vim.client.factory.create('ns0:VirtualPointingDeviceBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable', 'hostPointingDevice' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    