
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TaskInfo(vim, *args, **kwargs):
    '''This data object type contains all information about a task. A task represents
    an operation performed by VirtualCenter or ESX.'''
    
    obj = vim.client.factory.create('ns0:TaskInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 10 arguments got: %d' % len(args))

    required = [ 'cancelable', 'cancelled', 'descriptionId', 'eventChainId', 'key', 'queueTime',
        'reason', 'state', 'task' ]
    optional = [ 'changeTag', 'completeTime', 'description', 'entity', 'entityName', 'error',
        'locked', 'name', 'parentTaskKey', 'progress', 'result', 'rootTaskKey',
        'startTime', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    