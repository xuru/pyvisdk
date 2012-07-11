
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmTriggeringActionTransitionSpec(vim, *args, **kwargs):
    '''Specification indicating which on transitions this action fires. The existence
    of a Spec indicates that this action fires on transitions from that Spec's
    startState to finalState.There are only four acceptable {startState,
    finalState} pairs: {green, yellow}, {yellow, red}, {red, yellow} and {yellow,
    green}. At least one of these pairs must be specified. Any deviation from the
    above will render the enclosing AlarmSpec invalid.'''
    
    obj = vim.client.factory.create('ns0:AlarmTriggeringActionTransitionSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'finalState', 'repeats', 'startState' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    