# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineRelocateSpecDiskLocator(vim, *args, **kwargs):
    '''The DiskLocator data object type specifies a virtual disk device (by ID) and a
    datastore locator for the disk's storage.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineRelocateSpecDiskLocator')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastore', 'diskId', 'diskMoveType' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    