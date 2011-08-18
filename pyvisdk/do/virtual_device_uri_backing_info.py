# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceURIBackingInfo(vim, *args, **kwargs):
    '''The data object type defines information for using a network socket as backing
    for a virtual device.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceURIBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'direction', 'proxyURI', 'serviceURI' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    