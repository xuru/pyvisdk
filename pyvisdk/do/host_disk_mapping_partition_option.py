# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskMappingPartitionOption(vim, *args, **kwargs):
    '''The PhysicalPartitionOption data class contains the options for a partition on
    a physical disk.'''
    
    obj = vim.client.factory.create('ns0:HostDiskMappingPartitionOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'capacityInKb', 'fileSystem', 'name' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    