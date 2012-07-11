
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualHardware(vim, *args, **kwargs):
    '''The VirtualHardware data object type contains the complete configuration of the
    hardware in a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualHardware')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'memoryMB', 'numCPU' ]
    optional = [ 'device', 'numCoresPerSocket', 'virtualICH7MPresent', 'virtualSMCPresent',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    