# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFibreChannelHba(vim, *args, **kwargs):
    '''This data object type describes the Fibre Channel host bus adapter.'''
    
    obj = vim.client.factory.create('ns0:HostFibreChannelHba')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bus', 'device', 'driver', 'key', 'model', 'pci', 'status',
        'nodeWorldWideName', 'portType', 'portWorldWideName', 'speed' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    