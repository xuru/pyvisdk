# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFileSystemVolume(vim, *args, **kwargs):
    '''Detailed information about a file system. This is a base type for derived types
    that have more specific details about specific filesystem types.Typically a
    FileSystem is exposed as a datatore See DatastoreInfo See HostVmfsVolume See
    HostNasVolume See HostLocalFileSystemVolume'''
    
    obj = vim.client.factory.create('ns0:HostFileSystemVolume')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'capacity', 'name', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    