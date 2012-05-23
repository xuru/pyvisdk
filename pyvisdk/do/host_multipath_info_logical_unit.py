
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfoLogicalUnit(vim, *args, **kwargs):
    '''The HostMultipathInfoLogicalUnit data object represents a storage entity that
    provides disk blocks to a host.'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfoLogicalUnit')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'id', 'key', 'lun', 'path', 'policy' ]
    optional = [ 'storageArrayTypePolicy', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    