
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineDefaultPowerOpInfo(vim, *args, **kwargs):
    '''The DefaultPowerOpInfo data object type holds the configured defaults for the
    power operations on a virtual machine. The properties indicated whether to do a
    "soft" or guest initiated operation, or a "hard" operation.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineDefaultPowerOpInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'defaultPowerOffType', 'defaultResetType', 'defaultSuspendType',
        'powerOffType', 'resetType', 'standbyAction', 'suspendType', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    