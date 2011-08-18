# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualUSBRemoteHostBackingOption(vim, *args, **kwargs):
    '''The VirtualUSBRemoteHostBackingOption data object contains options for remote
    host USB configuration. This backing option indicates support for persistent
    USB connections when vMotion operations migrate virtual machines to different
    hosts.'''
    
    obj = vim.client.factory.create('ns0:VirtualUSBRemoteHostBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    