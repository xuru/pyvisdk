# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPCIPassthrough(vim, *args, **kwargs):
    '''The VirtualPCIPassthrough data object type contains information about a PCI
    device on the virtual machine that is being backed by a generic PCI device on
    the host via passthrough.'''
    
    obj = vim.client.factory.create('ns0:VirtualPCIPassthrough')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'key', 'unitNumber' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    