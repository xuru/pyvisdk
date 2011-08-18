# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionSpec(vim, *args, **kwargs):
    '''This data object type describes the disk partition table specification used to
    configure the partitions on a disk. This data object represents the fundamental
    data needed to specify a partition table.'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chs', 'partition', 'totalSectors' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    