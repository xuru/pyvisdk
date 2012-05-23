
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPlugStoreTopologyAdapter(vim, *args, **kwargs):
    '''This data object type is an association class that describes a host bus adapter
    and its associated storage Paths. The set of Paths on all the host bus adapters
    is the complete set of Paths in the system.'''
    
    obj = vim.client.factory.create('ns0:HostPlugStoreTopologyAdapter')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'adapter', 'key' ]
    optional = [ 'path', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    