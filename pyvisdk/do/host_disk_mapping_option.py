# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskMappingOption(vim, *args, **kwargs):
    '''The HostDiskMappingOption data object type describes the options for a virtual
    disk mapping to a host disk.'''
    
    obj = vim.client.factory.create('ns0:HostDiskMappingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name', 'physicalPartition' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    