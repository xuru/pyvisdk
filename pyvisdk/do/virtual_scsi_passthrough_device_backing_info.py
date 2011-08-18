# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSCSIPassthroughDeviceBackingInfo(vim, *args, **kwargs):
    '''The VirtualSCSIPassthrough.DeviceBackingInfo data object type contains
    information about the backing that maps the virtual device onto a physical
    device.'''
    
    obj = vim.client.factory.create('ns0:VirtualSCSIPassthroughDeviceBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    