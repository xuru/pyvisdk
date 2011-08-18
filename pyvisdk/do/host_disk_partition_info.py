# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionInfo(vim, *args, **kwargs):
    '''Information about the partitions on a disk. A DiskPartitionInfo object provides
    two different views into the partitions on a disk:* A detailed specification
    that is used to create the partition table. * A convenient view that shows the
    allocations of blocks as a contiguous sequence of block ranges.See
    RetrieveDiskPartitionInfo See ComputeDiskPartitionInfo See UpdateDiskPartitions'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'layout', 'spec' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    