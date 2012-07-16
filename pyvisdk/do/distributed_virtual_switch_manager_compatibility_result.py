
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchManagerCompatibilityResult(vim, *args, **kwargs):
    '''This is the return type for the checkCompatibility method. This object has a
    host property and optionally a fault which would be populated only if that host
    is not compatible with a given dvsProductSpec. If the host is compatible then
    the error property would be unset.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchManagerCompatibilityResult')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'host' ]
    optional = [ 'error', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    