# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceBackingInfo(vim, *args, **kwargs):
    '''is a base data object type for information about the backing of a device in a
    virtual machine. This base type does not define any properties. It is used as a
    namespace for general-purpose subtypes. Specific devices are represented by
    subtypes which define properties for device-specific backing information.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [  ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    