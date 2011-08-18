# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ScheduledTaskInfo(vim, *args, **kwargs):
    '''The scheduled task details.'''
    
    obj = vim.client.factory.create('ns0:ScheduledTaskInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'action', 'description', 'enabled', 'name', 'notification', 'scheduler',
        'activeTask', 'entity', 'error', 'lastModifiedTime', 'lastModifiedUser',
        'nextRunTime', 'prevRunTime', 'progress', 'result', 'scheduledTask', 'state',
        'taskObject' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    