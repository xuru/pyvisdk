
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfoFixedLogicalUnitPolicy(vim, *args, **kwargs):
    '''The HostMultipathInfoFixedLogicalUnitPolicy data object describes a
    multipathing policy for a logical unit which uses a preferred path whenever
    possible.'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfoFixedLogicalUnitPolicy')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'prefer', 'policy' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    