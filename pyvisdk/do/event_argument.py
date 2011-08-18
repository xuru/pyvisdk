# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventArgument(vim, *args, **kwargs):
    '''This is the base type for event argument types.Event argument objects, which
    inherit from a common subtype, are used to manage supplementary properties of
    different kinds of event objects.'''
    
    obj = vim.client.factory.create('ns0:EventArgument')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [  ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    