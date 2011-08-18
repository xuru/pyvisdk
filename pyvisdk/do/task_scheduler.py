# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TaskScheduler(vim, *args, **kwargs):
    '''The TaskScheduler data object is the base type for the scheduler objects. The
    hierarchy of scheduler objects is as follows:Use a scheduler object to set the
    time(s) for task execution. You can use two scheduling modes - single execution
    or recurring execution:* Use the AfterStartupTaskScheduler or the
    OnceTaskScheduler to schedule a single instance of task execution. * Use one of
    the recurrent task schedulers to schedule hourly, daily, weekly, or monthly
    task execution.After you have established the task timing, use the scheduler
    object for the ScheduledTaskSpec scheduler property value.'''
    
    obj = vim.client.factory.create('ns0:TaskScheduler')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeTime', 'expireTime' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    