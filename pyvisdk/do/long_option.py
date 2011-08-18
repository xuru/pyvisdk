# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def LongOption(vim, *args, **kwargs):
    '''The LongOption data object type is used to define the minimum, maximum, and
    default values for a 64-bit long option.'''
    
    obj = vim.client.factory.create('ns0:LongOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'valueIsReadonly', 'defaultValue', 'max', 'min' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    