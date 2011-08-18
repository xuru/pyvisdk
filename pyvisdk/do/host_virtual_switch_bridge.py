# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualSwitchBridge(vim, *args, **kwargs):
    '''A bridge connects a virtual switch to a physical network adapter. There are
    multiple types of bridges.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualSwitchBridge')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [  ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    