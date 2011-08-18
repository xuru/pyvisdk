# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StringOption(vim, *args, **kwargs):
    '''The StringOption data object type is used to define an open-ended string value
    based on an optional subset of valid characters.'''
    
    obj = vim.client.factory.create('ns0:StringOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'valueIsReadonly', 'defaultValue', 'validCharacters' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    