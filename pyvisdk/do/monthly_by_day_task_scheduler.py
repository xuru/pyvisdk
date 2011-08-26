
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def MonthlyByDayTaskScheduler(vim, *args, **kwargs):
    '''By default the scheduler executes the task on the specified day every month. If
    you set the interval to a value greater than 1, the task will execute at the
    specified monthly interval. (For example, an interval of 2 will cause the task
    to execute on the specified day, hour, and minute every 2 months.)'''
    
    obj = vim.client.factory.create('ns0:MonthlyByDayTaskScheduler')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'interval', 'minute', 'hour', 'day' ]
    inherited = [ 'activeTime', 'expireTime' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    