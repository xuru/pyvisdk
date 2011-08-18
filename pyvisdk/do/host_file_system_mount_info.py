# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFileSystemMountInfo(vim, *args, **kwargs):
    '''The HostFileSystemMountInfo data object describes a host mount point for a file
    system.'''
    
    obj = vim.client.factory.create('ns0:HostFileSystemMountInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'mountInfo', 'volume', 'vStorageSupport' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    