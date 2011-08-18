# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDisk(vim, *args, **kwargs):
    '''This data object type contains information about a disk in a virtual
    machine.The virtual disk backing object types describe the different virtual
    disk backings available. The disk format version in each case describes the
    version of the format that is used.Supported virtual disk backings:'''
    
    obj = vim.client.factory.create('ns0:VirtualDisk')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'key', 'unitNumber',
        'capacityInKB', 'shares', 'storageIOAllocation' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    