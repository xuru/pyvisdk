
import logging
from pyvisdk.exceptions import InvalidArgumentError

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
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'activeTime', 'expireTime', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    