# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVmfsSpec(vim, *args, **kwargs):
    '''This data object type describes the VMware File System (VMFS) creation
    specification. Once created, these properties for the most part cannot be
    changed. There are a few exceptions.'''
    
    obj = vim.client.factory.create('ns0:HostVmfsSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'blockSizeMb', 'extent', 'majorVersion', 'volumeName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    