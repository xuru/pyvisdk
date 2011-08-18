# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StorageIOAllocationInfo(vim, *args, **kwargs):
    '''The IOAllocationInfo specifies the shares and the limit for storage I/O
    resource.The storage I/O resource is allocated to virtual machines based on
    their shares and limit. We do not support reservation for storage I/O resource.
    And we do not support storage I/O resource management on resource pools.Each
    virtual machine has one IOAllocationInfo object per virtual disk. For example,
    we can specify that a virtual machine has 500 shares on the first virtual disk,
    1000 shares on the second virtual disk, etc.'''
    
    obj = vim.client.factory.create('ns0:StorageIOAllocationInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'limit', 'shares' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    