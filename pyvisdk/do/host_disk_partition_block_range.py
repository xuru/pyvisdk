# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionBlockRange(vim, *args, **kwargs):
    '''A BlockRange data object type describes a contiguous set of blocks on a disk. A
    BlockRange may describe either a partition or unpartitioned (primordial) blocks
    on the disk.'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionBlockRange')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'end', 'partition', 'start', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    