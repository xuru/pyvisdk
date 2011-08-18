# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DailyTaskScheduler(vim, *args, **kwargs):
    '''The DailyTaskScheduler data object sets the time for daily task execution. You
    set the hour and the inherited minute property to complete the schedule. By
    default, the scheduled task will run once every day at the specified hour and
    minute.If you set the interval to a value greater than 1, the task will execute
    at the specified daily interval. (For example, an interval of 2 will cause the
    task to execute at the specified hour and minute every 2 days.)'''
    
    obj = vim.client.factory.create('ns0:DailyTaskScheduler')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeTime', 'expireTime', 'interval', 'minute', 'hour' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    