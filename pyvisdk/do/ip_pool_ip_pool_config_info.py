
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def IpPoolIpPoolConfigInfo(vim, *args, **kwargs):
    '''Specifications of either IPv4 or IPv6 configuration to be used on this network.
    This is a part of network configuration.IPv4 addresses are in dot-decimal
    notation, e.g.: 192.0.2.235IPv6 addresses are in colon-hexadecimal notation,
    e.g.: 2001:0db8:85a3::0370:7334'''
    
    obj = vim.client.factory.create('ns0:IpPoolIpPoolConfigInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'dhcpServerAvailable', 'dns', 'gateway', 'ipPoolEnabled', 'netmask', 'range',
        'subnetAddress', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    