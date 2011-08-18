# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualFloppyRemoteDeviceBackingOption(vim, *args, **kwargs):
    '''The RemoteDeviceBackingOption data object type contains the options for the
    floppy remote device backing type.'''
    
    obj = vim.client.factory.create('ns0:VirtualFloppyRemoteDeviceBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    