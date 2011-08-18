# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceBackingOption(vim, *args, **kwargs):
    '''The VirtualDeviceBackingOption data class defines options for device-specific
    virtual backing objects.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    