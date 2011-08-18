# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def MonthlyTaskScheduler(vim, *args, **kwargs):
    '''The MonthlyTaskScheduler data object is the base type for the monthly
    schedulers (MonthlyByDayTaskScheduler and MonthlyByWeekdayTaskScheduler).'''
    
    obj = vim.client.factory.create('ns0:MonthlyTaskScheduler')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'activeTime', 'expireTime', 'interval', 'minute', 'hour' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    