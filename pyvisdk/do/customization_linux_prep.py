
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationLinuxPrep(vim, *args, **kwargs):
    '''This is the Linux counterpart to the Windows Sysprep object. LinuxPrep contains
    machine-wide settings that identify a Linux machine in the same way that the
    Sysprep type identifies a Windows machine.'''
    
    obj = vim.client.factory.create('ns0:CustomizationLinuxPrep')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'domain', 'hostName' ]
    optional = [ 'hwClockUTC', 'timeZone', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    