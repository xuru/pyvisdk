# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachinePciPassthroughInfo(vim, *args, **kwargs):
    '''Description of a generic PCI device that can be attached to a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachinePciPassthroughInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configurationTag', 'name', 'pciDevice', 'systemId' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    