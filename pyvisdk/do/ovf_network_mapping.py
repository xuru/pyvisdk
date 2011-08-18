# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfNetworkMapping(vim, *args, **kwargs):
    '''A NetworkMapping is a choice made by the caller about which VI network to use
    for a specific network in the OVF descriptor.'''
    
    obj = vim.client.factory.create('ns0:OvfNetworkMapping')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name', 'network' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    