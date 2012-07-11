
import logging
from pyvisdk.exceptions import InvalidArgumentError

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
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'minute', 'interval' ]
    optional = [ 'activeTime', 'expireTime', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    