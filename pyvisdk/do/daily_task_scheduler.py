
import logging
from pyvisdk.exceptions import InvalidArgumentError

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
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'hour', 'minute', 'interval' ]
    optional = [ 'activeTime', 'expireTime', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    