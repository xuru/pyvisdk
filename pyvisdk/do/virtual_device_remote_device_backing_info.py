# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceRemoteDeviceBackingInfo(vim, *args, **kwargs):
    '''is a data object type for information about a remote device backing used by a
    device in a virtual machine. The primary difference between a remote device
    backing and a local device backing is that the VirtualCenter server cannot
    provide a list of remote host devices available for this virtual device
    backing.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceRemoteDeviceBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    