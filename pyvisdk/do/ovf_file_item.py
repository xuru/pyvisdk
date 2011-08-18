# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfFileItem(vim, *args, **kwargs):
    '''An FileItem represents a file that must be uploaded by the caller when the
    inventory objects has been created in VI. These objects are created by
    ResourcePool.importVApp.Files can either be new files, in which case the
    "create" flag will be true, or updates to existing files in VI. The latter is
    used to support the OVF parentRef mechanism for Disks.'''
    
    obj = vim.client.factory.create('ns0:OvfFileItem')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chunkSize', 'cimType', 'compressionMethod', 'create', 'deviceId', 'path',
        'size' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    