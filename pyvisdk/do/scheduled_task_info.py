
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ScheduledTaskInfo(vim, *args, **kwargs):
    '''The scheduled task details.'''
    
    obj = vim.client.factory.create('ns0:ScheduledTaskInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 11:
        raise IndexError('Expected at least 12 arguments got: %d' % len(args))

    required = [ 'entity', 'lastModifiedTime', 'lastModifiedUser', 'scheduledTask', 'state',
        'taskObject', 'action', 'description', 'enabled', 'name', 'scheduler' ]
    optional = [ 'activeTask', 'error', 'nextRunTime', 'prevRunTime', 'progress', 'result',
        'notification', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    