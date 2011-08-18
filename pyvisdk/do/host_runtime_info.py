# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostRuntimeInfo(vim, *args, **kwargs):
    '''This data object type describes the runtime state of a host.'''
    
    obj = vim.client.factory.create('ns0:HostRuntimeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bootTime', 'connectionState', 'healthSystemRuntime', 'inMaintenanceMode',
        'powerState', 'standbyMode', 'tpmPcrValues' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    