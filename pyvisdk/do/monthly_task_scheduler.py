
import logging
from pyvisdk.exceptions import InvalidArgumentError

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
    