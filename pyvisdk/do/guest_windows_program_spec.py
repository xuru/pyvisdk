
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def GuestWindowsProgramSpec(vim, *args, **kwargs):
    '''This describes the arguments to StartProgramInGuest that apply only for Windows
    guests.'''
    
    obj = vim.client.factory.create('ns0:GuestWindowsProgramSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'startMinimized', 'arguments', 'programPath' ]
    optional = [ 'envVariables', 'workingDirectory', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    