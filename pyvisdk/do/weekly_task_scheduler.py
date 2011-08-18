# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def WeeklyTaskScheduler(vim, *args, **kwargs):
    '''The WeeklyTaskScheduler data object sets the time for weekly task execution.
    You can set the schedule for task execution on one or more days during the
    week, and you complete the schedule by setting the inherited properties for the
    hour and minute.By default the scheduler executes the task according to the
    specified day(s) every week. If you set the interval to a value greater than 1,
    the task will execute at the specified weekly interval. (For example, an
    interval of 2 will cause the task to execute on the specified days every 2
    weeks.)'''
    
    obj = vim.client.factory.create('ns0:WeeklyTaskScheduler')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 10:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeTime', 'expireTime', 'interval', 'minute', 'hour', 'friday', 'monday',
        'saturday', 'sunday', 'thursday', 'tuesday', 'wednesday' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    