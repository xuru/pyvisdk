# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostUnresolvedVmfsResolutionResult(vim, *args, **kwargs):
    '''When an UnresolvedVmfsVolume has been resignatured or forceMounted, we want to
    return the original spec information along with newly created VMFS volume.'''
    
    obj = vim.client.factory.create('ns0:HostUnresolvedVmfsResolutionResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'fault', 'spec', 'vmfs' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    