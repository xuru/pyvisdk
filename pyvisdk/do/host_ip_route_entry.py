
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostIpRouteEntry(vim, *args, **kwargs):
    '''IpRouteEntry. Routing entries are individual static routes which combined with
    the default route form all of the routing rules for a host.'''
    
    obj = vim.client.factory.create('ns0:HostIpRouteEntry')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'gateway', 'network', 'prefixLength' ]
    optional = [ 'deviceName', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    