# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPointingDeviceDeviceBackingInfo(vim, *args, **kwargs):
    '''The VirtualPointingDevice.DeviceBackingInfo provides information about the
    physical mouse backing the VirtualPointingDevice data object type.'''
    
    obj = vim.client.factory.create('ns0:VirtualPointingDeviceDeviceBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect', 'hostPointingDevice' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    