
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostUnresolvedVmfsResolutionResult(vim, *args, **kwargs):
    '''When an UnresolvedVmfsVolume has been resignatured or forceMounted, we want to
    return the original spec information along with newly created VMFS volume.'''
    
    obj = vim.client.factory.create('ns0:HostUnresolvedVmfsResolutionResult')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'spec' ]
    optional = [ 'fault', 'vmfs', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    