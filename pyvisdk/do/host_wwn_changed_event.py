
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostWwnChangedEvent(vim, *args, **kwargs):
    '''This event records a change in a host's WWN (World Wide Name).'''
    
    obj = vim.client.factory.create('ns0:HostWwnChangedEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'newNodeWwns', 'newPortWwns', 'oldNodeWwns', 'oldPortWwns', 'changeTag',
        'computeResource', 'datacenter', 'ds', 'dvs', 'fullFormattedMessage', 'host',
        'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    