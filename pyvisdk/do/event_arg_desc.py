# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventArgDesc(vim, *args, **kwargs):
    '''Describes an available event argument name for an Event type, which can be used
    in EventAlarmExpression.'''
    
    obj = vim.client.factory.create('ns0:EventArgDesc')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'description', 'name', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    