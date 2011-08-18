# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNicNameHint(vim, *args, **kwargs):
    '''This data object type describes a network in network hint where the network
    describes the color, label, or the name of the network.'''
    
    obj = vim.client.factory.create('ns0:PhysicalNicNameHint')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'vlanId', 'network' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    