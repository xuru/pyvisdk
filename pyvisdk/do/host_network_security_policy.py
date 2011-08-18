# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkSecurityPolicy(vim, *args, **kwargs):
    '''This data object type describes security policy governing ports.'''
    
    obj = vim.client.factory.create('ns0:HostNetworkSecurityPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'allowPromiscuous', 'forgedTransmits', 'macChanges' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    