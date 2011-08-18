# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualSwitch(vim, *args, **kwargs):
    '''The virtual switch is a software entity to which multiple virtual network
    adapters can connect to create a virtual network. It can also be bridged to a
    physical network.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualSwitch')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'key', 'mtu', 'name', 'numPorts', 'numPortsAvailable', 'pnic', 'portgroup',
        'spec' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    