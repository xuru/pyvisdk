# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CreateTaskAction(vim, *args, **kwargs):
    '''This data object type specifies the type of task to be created when this action
    is triggered.'''
    
    obj = vim.client.factory.create('ns0:CreateTaskAction')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cancelable', 'taskTypeId' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    