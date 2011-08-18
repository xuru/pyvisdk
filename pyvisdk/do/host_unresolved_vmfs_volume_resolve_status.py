# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostUnresolvedVmfsVolumeResolveStatus(vim, *args, **kwargs):
    '''Data object that describes the resolvability of a volume.'''
    
    obj = vim.client.factory.create('ns0:HostUnresolvedVmfsVolumeResolveStatus')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'incompleteExtents', 'multipleCopies', 'resolvable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    