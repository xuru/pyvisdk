# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMountInfo(vim, *args, **kwargs):
    '''The HostMountInfo data object provides information related to a configured
    mount point. This object does not include information about the mounted file
    system. (See HostFileSystemMountInfo.)'''
    
    obj = vim.client.factory.create('ns0:HostMountInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'accessible', 'accessMode', 'path' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    