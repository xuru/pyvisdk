
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventFilterSpec(vim, *args, **kwargs):
    '''Event filter used to query events in the history collector database. The client
    creates an event history collector with a filter specification, then retrieves
    the events from the event history collector.'''
    
    obj = vim.client.factory.create('ns0:EventFilterSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'alarm', 'category', 'disableFullMessage', 'entity', 'eventChainId',
        'eventTypeId', 'scheduledTask', 'tag', 'time', 'type', 'userName',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    