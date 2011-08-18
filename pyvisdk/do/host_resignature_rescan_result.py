# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostResignatureRescanResult(vim, *args, **kwargs):
    '''When a user resignatures an UnresolvedVmfsVolume through DatastoreSystem API,
    we resignature and auto-mount on the other hosts which share the same
    underlying storage luns. As part of the operation, we rescan the specified list
    of hosts. This data object describes the return value of resignature APIs in
    DatastoreSystem.'''
    
    obj = vim.client.factory.create('ns0:HostResignatureRescanResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'rescan', 'result' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    