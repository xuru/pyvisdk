
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPlugStoreTopologyPlugin(vim, *args, **kwargs):
    '''This data object type represents a Plugin in the plug store architecture. A
    Plugin claims a set of paths and groups them into Devices.'''
    
    obj = vim.client.factory.create('ns0:HostPlugStoreTopologyPlugin')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'key', 'name' ]
    optional = [ 'claimedPath', 'device', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    