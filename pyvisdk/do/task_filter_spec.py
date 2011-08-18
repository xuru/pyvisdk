# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TaskFilterSpec(vim, *args, **kwargs):
    '''This data object type defines the specification for the task filter used to
    query tasks in the history collector database. The client creates a task
    history collector with a filter specification, then retrieves the tasks from
    the task history collector.'''
    
    obj = vim.client.factory.create('ns0:TaskFilterSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'alarm', 'entity', 'eventChainId', 'parentTaskKey', 'rootTaskKey',
        'scheduledTask', 'state', 'tag', 'time', 'userName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    