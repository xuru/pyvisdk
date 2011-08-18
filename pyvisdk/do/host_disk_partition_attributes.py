# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionAttributes(vim, *args, **kwargs):
    '''Information about a single disk partition. A partition is a contiguous set of
    blocks on a disk that is marked for use. The typeId identifies the purpose of
    the data in the partition.'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionAttributes')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'attributes', 'endSector', 'logical', 'partition', 'startSector', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    