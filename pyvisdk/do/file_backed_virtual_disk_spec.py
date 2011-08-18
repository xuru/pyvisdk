# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FileBackedVirtualDiskSpec(vim, *args, **kwargs):
    '''Specification used to create a file based virtual disk'''
    
    obj = vim.client.factory.create('ns0:FileBackedVirtualDiskSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'adapterType', 'diskType', 'capacityKb' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    