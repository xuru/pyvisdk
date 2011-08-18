# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSoundCardDeviceBackingOption(vim, *args, **kwargs):
    '''The VirtualSoundCardBackingOption class contains the options for the virtual
    sound card backing class.'''
    
    obj = vim.client.factory.create('ns0:VirtualSoundCardDeviceBackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    