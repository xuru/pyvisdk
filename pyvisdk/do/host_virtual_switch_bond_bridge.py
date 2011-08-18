# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualSwitchBondBridge(vim, *args, **kwargs):
    '''This data object type describes a bridge that provides network adapter teaming
    capabilities.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualSwitchBondBridge')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'beacon', 'linkDiscoveryProtocolConfig', 'nicDevice' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    