# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def BoolOption(vim, *args, **kwargs):
    '''The BoolOption data object type describes if an option is supported ("true")
    and if the option is set to "true" or "false" by default.'''
    
    obj = vim.client.factory.create('ns0:BoolOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'valueIsReadonly', 'defaultValue', 'supported' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    