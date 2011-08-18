# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfNetworkInfo(vim, *args, **kwargs):
    '''The name and description of a network as specified by the OVF descriptor.'''
    
    obj = vim.client.factory.create('ns0:OvfNetworkInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'description', 'name' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    