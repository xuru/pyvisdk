# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDevice(vim, *args, **kwargs):
    '''VirtualDevice is the base data object type for devices in a virtual machine.
    This type contains enough information about a virtual device to allow clients
    to display devices they do not recognize. For example, a client with an older
    version than the server to which it connects may see a device without knowing
    what it is.'''
    
    obj = vim.client.factory.create('ns0:VirtualDevice')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'key', 'unitNumber' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    