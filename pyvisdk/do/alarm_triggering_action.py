
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmTriggeringAction(vim, *args, **kwargs):
    '''This data object type describes one or more triggering transitions and an
    action to be done when an alarm is triggered.There are four triggering
    transitions; at least one of them must be provided. A gray state is considered
    the same as a green state, for the purpose of detecting transitions.'''
    
    obj = vim.client.factory.create('ns0:AlarmTriggeringAction')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'action', 'green2yellow', 'red2yellow', 'yellow2green', 'yellow2red' ]
    optional = [ 'transitionSpecs', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    