
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreCapacityIncreasedEvent(vim, *args, **kwargs):
    '''This event records when increase in a datastore's capacity is observed. It may
    happen due to different reasons, like extending or expanding a datastore.'''
    
    obj = vim.client.factory.create('ns0:DatastoreCapacityIncreasedEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'newCapacity', 'oldCapacity', 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'datastore', 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    