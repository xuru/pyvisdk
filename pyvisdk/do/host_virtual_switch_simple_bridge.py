# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualSwitchSimpleBridge(vim, *args, **kwargs):
    '''A bridge that is statically bound to a single physical network adapter.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualSwitchSimpleBridge')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'nicDevice' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    