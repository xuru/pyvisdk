# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskMappingInfo(vim, *args, **kwargs):
    '''The HostDiskMappingInfo data object type describes a virtual disk mapping to a
    host disk.'''
    
    obj = vim.client.factory.create('ns0:HostDiskMappingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'exclusive', 'name', 'physicalPartition' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    