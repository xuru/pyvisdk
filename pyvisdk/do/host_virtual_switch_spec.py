# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualSwitchSpec(vim, *args, **kwargs):
    '''This data object type describes the VirtualSwitch specification representing
    the properties on a VirtualSwitch that can be configured once the object
    exists.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualSwitchSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bridge', 'mtu', 'numPorts', 'policy' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    