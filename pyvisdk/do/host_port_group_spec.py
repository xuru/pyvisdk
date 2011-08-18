# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPortGroupSpec(vim, *args, **kwargs):
    '''This data object type describes the PortGroup specification representing the
    properties on a PortGroup that can be configured.'''
    
    obj = vim.client.factory.create('ns0:HostPortGroupSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name', 'policy', 'vlanId', 'vswitchName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    