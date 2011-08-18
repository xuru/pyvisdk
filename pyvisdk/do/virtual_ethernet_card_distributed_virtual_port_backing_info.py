# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualEthernetCardDistributedVirtualPortBackingInfo(vim, *args, **kwargs):
    '''The class defines a VirtualEthernetCard backing that connects the device to a
    distributed virtual switch port or portgroup.'''
    
    obj = vim.client.factory.create('ns0:VirtualEthernetCardDistributedVirtualPortBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'port' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    