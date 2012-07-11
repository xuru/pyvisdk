
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def LockerReconfiguredEvent(vim, *args, **kwargs):
    '''Locker was reconfigured to a new location.'''
    
    obj = vim.client.factory.create('ns0:LockerReconfiguredEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'newDatastore', 'oldDatastore', 'changeTag', 'computeResource', 'datacenter',
        'ds', 'dvs', 'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    