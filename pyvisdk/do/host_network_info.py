
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkInfo(vim, *args, **kwargs):
    '''This data object type describes networking host configuration data objects.'''
    
    obj = vim.client.factory.create('ns0:HostNetworkInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'atBootIpV6Enabled', 'consoleIpRouteConfig', 'consoleVnic', 'dhcp',
        'dnsConfig', 'ipRouteConfig', 'ipV6Enabled', 'nat', 'pnic', 'portgroup',
        'proxySwitch', 'routeTableInfo', 'vnic', 'vswitch', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    