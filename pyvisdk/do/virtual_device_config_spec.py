
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDeviceConfigSpec(vim, *args, **kwargs):
    '''The VirtualDeviceSpec data object type encapsulates change specifications for
    an individual virtual device. The virtual device being added or modified must
    be fully specified.'''
    
    obj = vim.client.factory.create('ns0:VirtualDeviceConfigSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'device' ]
    optional = [ 'fileOperation', 'operation', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    