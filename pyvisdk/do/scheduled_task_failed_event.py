
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ScheduledTaskFailedEvent(vim, *args, **kwargs):
    '''This event records the failure of a scheduled task.'''
    
    obj = vim.client.factory.create('ns0:ScheduledTaskFailedEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'reason', 'entity', 'scheduledTask', 'chainId', 'createdTime', 'key',
        'userName' ]
    optional = [ 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    