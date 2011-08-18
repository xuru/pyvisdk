# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceConnectOption(vim, *args, **kwargs):
    '''The ConnectOption data object type contains information about options for
    connectable virtual devices.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceConnectOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'allowGuestControl', 'startConnected' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    