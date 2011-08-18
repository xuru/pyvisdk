# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineFileLayoutExDiskUnit(vim, *args, **kwargs):
    '''Information about a single unit of a virtual disk, such as the base-disk or a
    delta-disk.A disk-unit consists of at least one descriptor file, and zero or
    more extent files.Sometimes, a disk-unit is also referred to as a .'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineFileLayoutExDiskUnit')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'fileKey' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    