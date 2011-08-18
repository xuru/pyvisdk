# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFlagInfo(vim, *args, **kwargs):
    '''The FlagInfo data object type encapsulates the flag settings for a host. These
    properties are optional since the same structure is used to change the values
    during an edit or create operation.'''
    
    obj = vim.client.factory.create('ns0:HostFlagInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backgroundSnapshotsEnabled' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    