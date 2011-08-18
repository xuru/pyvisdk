# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def Action(vim, *args, **kwargs):
    '''This data object type defines the action initiated by a scheduled task or
    alarm.This is an abstract type. A client creates a scheduled task or an alarm
    each of which triggers an action, defined by a subclass of this type.'''
    
    obj = vim.client.factory.create('ns0:Action')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [  ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    