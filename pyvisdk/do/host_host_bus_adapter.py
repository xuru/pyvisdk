# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHostBusAdapter(vim, *args, **kwargs):
    '''This data object type describes the bus adapter for the host. A host bus
    adapter (HBA) is a hardware or software adapter that connects the host to
    storage devices.'''
    
    obj = vim.client.factory.create('ns0:HostHostBusAdapter')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bus', 'device', 'driver', 'key', 'model', 'pci', 'status' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    