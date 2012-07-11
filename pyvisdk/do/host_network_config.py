
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkConfig(vim, *args, **kwargs):
    '''This data object type describes networking host configuration data objects.
    These objects contain only the configuration information for networking. The
    runtime information is available from the NetworkInfo data object type.See
    HostNetworkInfo'''
    
    obj = vim.client.factory.create('ns0:HostNetworkConfig')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'consoleIpRouteConfig', 'consoleVnic', 'dhcp', 'dnsConfig', 'ipRouteConfig',
        'ipV6Enabled', 'nat', 'pnic', 'portgroup', 'proxySwitch', 'routeTableConfig',
        'vnic', 'vswitch', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    