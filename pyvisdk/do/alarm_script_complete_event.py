
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmScriptCompleteEvent(vim, *args, **kwargs):
    '''This event records the completion of an alarm-triggered script.'''
    
    obj = vim.client.factory.create('ns0:AlarmScriptCompleteEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'entity', 'script', 'alarm', 'chainId', 'createdTime', 'key', 'userName' ]
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
    