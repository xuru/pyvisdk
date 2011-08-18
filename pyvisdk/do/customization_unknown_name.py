# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationUnknownName(vim, *args, **kwargs):
    '''Indicates that the name is not specified in advance. The client should prompt
    the user for the value to complete the specification.'''
    
    obj = vim.client.factory.create('ns0:CustomizationUnknownName')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [  ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    