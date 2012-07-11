
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmInfo(vim, *args, **kwargs):
    '''Attributes of an alarm.'''
    
    obj = vim.client.factory.create('ns0:AlarmInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 10:
        raise IndexError('Expected at least 11 arguments got: %d' % len(args))

    required = [ 'alarm', 'creationEventId', 'entity', 'key', 'lastModifiedTime',
        'lastModifiedUser', 'description', 'enabled', 'expression', 'name' ]
    optional = [ 'action', 'actionFrequency', 'setting', 'systemName', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    