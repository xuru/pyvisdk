# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchPortConnectee(vim, *args, **kwargs):
    '''Information about the entity that connects to a DistributedVirtualPort.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchPortConnectee')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'addressHint', 'connectedEntity', 'nicKey', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    