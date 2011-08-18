# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceConnectInfo(vim, *args, **kwargs):
    '''The data object type contains information about connectable virtual devices.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceConnectInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'allowGuestControl', 'connected', 'startConnected', 'status' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    