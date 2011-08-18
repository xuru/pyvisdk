# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionLayout(vim, *args, **kwargs):
    '''This data object type describes the disk partition layout specified as a list
    of ordered BlockRanges. This view of the disk partitions shows the data on the
    disk as a contiguous set of BlockRanges.'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionLayout')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'partition', 'total' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    