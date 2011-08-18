# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNicHintInfo(vim, *args, **kwargs):
    '''The NetworkHint data object type is some information about the network to which
    the physical network adapter is attached.'''
    
    obj = vim.client.factory.create('ns0:PhysicalNicHintInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'connectedSwitchPort', 'device', 'network', 'subnet' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    