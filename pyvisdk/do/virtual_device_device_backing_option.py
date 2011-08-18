# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceDeviceBackingOption(vim, *args, **kwargs):
    '''The DeviceBackingOption data class contains device-specific backing options.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceDeviceBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    