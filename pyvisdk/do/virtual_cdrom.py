
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdrom(vim, *args, **kwargs):
    '''The VirtualCdrom data object type describes the configuration of a CD-ROM
    device in a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdrom')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'key' ]
    optional = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'unitNumber',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    