
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDnsConfig(vim, *args, **kwargs):
    '''This data object type describes the DNS configuration.All IPv4 addresses,
    subnet addresses, and netmasks are specified using dotted decimal notation. For
    example, "192.0.2.1". IPv6 addresses are 128-bit addresses represented as eight
    fields of up to four hexadecimal digits. A colon separates each field (:). For
    example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the
    symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in
    an address as described in RFC 2373.'''
    
    obj = vim.client.factory.create('ns0:HostDnsConfig')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'dhcp', 'domainName', 'hostName' ]
    optional = [ 'address', 'searchDomain', 'virtualNicDevice', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    