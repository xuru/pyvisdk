# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ObjectContent(vim, *args, **kwargs):
    '''The ObjectContent data object type contains the contents retrieved for a single
    managed object.'''
    
    obj = vim.client.factory.create('ns0:ObjectContent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'missingSet', 'obj', 'propSet' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    