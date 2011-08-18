# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TaskEvent(vim, *args, **kwargs):
    '''This event records the creation of a Task. Note that the embedded TaskInfo
    object is a of the Task state at the time of its creation, so its state will
    always be "queued". To find the current status of the task, query for the
    current state of the Task using the eventChainId in the embedded TaskInfo
    object.'''
    
    obj = vim.client.factory.create('ns0:TaskEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm', 'info' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    