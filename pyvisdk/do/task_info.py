# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TaskInfo(vim, *args, **kwargs):
    '''This data object type contains all information about a task. A task represents
    an operation performed by VirtualCenter or ESX.'''
    
    obj = vim.client.factory.create('ns0:TaskInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cancelable', 'cancelled', 'changeTag', 'completeTime', 'description',
        'descriptionId', 'entity', 'entityName', 'error', 'eventChainId', 'key',
        'locked', 'name', 'parentTaskKey', 'progress', 'queueTime', 'reason', 'result',
        'rootTaskKey', 'startTime', 'state', 'task' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    