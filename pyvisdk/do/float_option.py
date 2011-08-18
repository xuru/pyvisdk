# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FloatOption(vim, *args, **kwargs):
    '''The FloatOption data object type defines the minimum, maximum, and default
    values for a float option.'''
    
    obj = vim.client.factory.create('ns0:FloatOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'valueIsReadonly', 'defaultValue', 'max', 'min' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    