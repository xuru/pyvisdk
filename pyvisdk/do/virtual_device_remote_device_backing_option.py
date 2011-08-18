# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceRemoteDeviceBackingOption(vim, *args, **kwargs):
    '''VirtualDeviceOption.RemoteDeviceBackingOption describes the options for a
    remote device backing. The primary difference between a remote device backing
    and a local device backing is that the VirtualCenter server cannot provide a
    list of remote host devices available for this virtual device backing.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceRemoteDeviceBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    