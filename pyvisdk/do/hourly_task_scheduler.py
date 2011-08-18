# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HourlyTaskScheduler(vim, *args, **kwargs):
    '''The HourlyTaskScheduler data object sets the time for hourly task execution. By
    default, the scheduled task will run once every hour, at the specified
    minute.If you set the interval to a value greater than 1, the task will execute
    at the specified hourly interval. (For example, an interval of 2 will cause the
    task to execute at the specified minute every 2 hours.)'''
    
    obj = vim.client.factory.create('ns0:HourlyTaskScheduler')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeTime', 'expireTime', 'interval', 'minute' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    