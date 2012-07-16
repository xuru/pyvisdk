
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConsolePreferences(vim, *args, **kwargs):
    '''Preferences for the legacy console application that affect the way it behaves
    during power operations on the virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConsolePreferences')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'closeOnPowerOffOrSuspend', 'enterFullScreenOnPowerOn', 'powerOnWhenOpened',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    