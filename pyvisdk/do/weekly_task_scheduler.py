# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

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
        raise IndexError('Expected at least 11 arguments got: %d' % len(args))
        
    signature = [ 'interval', 'minute', 'hour', 'friday', 'monday', 'saturday', 'sunday',
        'thursday', 'tuesday', 'wednesday' ]
    inherited = [ 'activeTime', 'expireTime' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    