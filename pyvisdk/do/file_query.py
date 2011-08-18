# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FileQuery(vim, *args, **kwargs):
    '''The data object type that describes the base query specification. Contains
    query filters and details that apply to every file. Querying only file details
    generally does not require opening files and so is an efficient query. Derived
    types add query parameters specific to the type of file.'''
    
    obj = vim.client.factory.create('ns0:FileQuery')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [  ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    