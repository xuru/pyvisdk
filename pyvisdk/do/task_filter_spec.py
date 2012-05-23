
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TaskFilterSpec(vim, *args, **kwargs):
    '''This data object type defines the specification for the task filter used to
    query tasks in the history collector database. The client creates a task
    history collector with a filter specification, then retrieves the tasks from
    the task history collector.'''
    
    obj = vim.client.factory.create('ns0:TaskFilterSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'alarm', 'entity', 'eventChainId', 'parentTaskKey', 'rootTaskKey',
        'scheduledTask', 'state', 'tag', 'time', 'userName', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    