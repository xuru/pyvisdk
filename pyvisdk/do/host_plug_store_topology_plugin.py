# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPlugStoreTopologyPlugin(vim, *args, **kwargs):
    '''This data object type represents a Plugin in the plug store architecture. A
    Plugin claims a set of paths and groups them into Devices.'''
    
    obj = vim.client.factory.create('ns0:HostPlugStoreTopologyPlugin')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'claimedPath', 'device', 'key', 'name' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    