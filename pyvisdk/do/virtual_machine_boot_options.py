
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineBootOptions(vim, *args, **kwargs):
    '''The VirtualMachineBootOptions data object defines the boot-time behavior of a
    virtual machine.You can use the delay options to specify a time interval during
    which you can enter the virtual machine BIOS setup. These options provide a
    solution for the situation that occurs when the console attaches to the virtual
    machine after the boot sequence has passed the BIOS setup entry point.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineBootOptions')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'bootDelay', 'bootOrder', 'bootRetryDelay', 'bootRetryEnabled',
        'enterBIOSSetup', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    