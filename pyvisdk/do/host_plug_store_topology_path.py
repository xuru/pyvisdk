
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPlugStoreTopologyPath(vim, *args, **kwargs):
    '''This data object type is an association class that describes a Path and its
    associated Device. A Path may be claimed by at most one Device.'''
    
    obj = vim.client.factory.create('ns0:HostPlugStoreTopologyPath')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'key', 'name' ]
    optional = [ 'adapter', 'channelNumber', 'device', 'lunNumber', 'target', 'targetNumber',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    