# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def MonthlyByWeekdayTaskScheduler(vim, *args, **kwargs):
    '''The MonthlyByWeekdayTaskScheduler data object sets the time for monthly task
    execution. You identify a single day for task execution by specifying the week
    of the month and day of the week, and you complete the schedule by setting the
    inherited properties for the hour and minute.By default, the scheduler executes
    the task on the specified day every month. If you set the interval to a value
    greater than 1, the task will execute at the specified monthly interval. (For
    example, an interval of 2 will cause the task to execute on the specified day,
    hour, and minute every 2 months.)'''
    
    obj = vim.client.factory.create('ns0:MonthlyByWeekdayTaskScheduler')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeTime', 'expireTime', 'interval', 'minute', 'hour', 'offset', 'weekday' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    