# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualUSBUSBBackingOption(vim, *args, **kwargs):
    '''The VirtualUSBUSBBackingOption data object contains the options for virtual
    backing for a USB device. This backing option indicates support for a local
    connection where the virtual machine will remain on the host to which the USB
    device is attached.'''
    
    obj = vim.client.factory.create('ns0:VirtualUSBUSBBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    