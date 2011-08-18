# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPciPassthruInfo(vim, *args, **kwargs):
    '''This data object provides information about the state of PciPassthru for all
    pci devices.'''
    
    obj = vim.client.factory.create('ns0:HostPciPassthruInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dependentDevice', 'id', 'passthruActive', 'passthruCapable', 'passthruEnabled' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    