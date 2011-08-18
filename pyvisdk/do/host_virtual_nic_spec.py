# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualNicSpec(vim, *args, **kwargs):
    '''This data object type describes the VirtualNic configuration containing both
    the configured properties on a VirtualNic and identification information.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualNicSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'distributedVirtualPort', 'ip', 'mac', 'mtu', 'portgroup', 'tsoEnabled' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    