# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineFileLayoutExDiskLayout(vim, *args, **kwargs):
    '''Layout of a virtual disk, including the base- and delta- disks.A virtual disk
    typically is made up of a chain of disk-units.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineFileLayoutExDiskLayout')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chain', 'key' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    