# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def GuestDiskInfo(vim, *args, **kwargs):
    '''Information about each virtual disk configured in the guest operating system.'''
    
    obj = vim.client.factory.create('ns0:GuestDiskInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'capacity', 'diskPath', 'freeSpace' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    