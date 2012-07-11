
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaIPProperties(vim, *args, **kwargs):
    '''The IP properties for the host bus adapter'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaIPProperties')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'dhcpConfigurationEnabled' ]
    optional = [ 'address', 'alternateDnsServerAddress', 'arpRedirectEnabled', 'defaultGateway',
        'ipv6Address', 'ipv6DefaultGateway', 'ipv6SubnetMask', 'jumboFramesEnabled',
        'mac', 'mtu', 'primaryDnsServerAddress', 'subnetMask', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    