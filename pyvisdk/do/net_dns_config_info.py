
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetDnsConfigInfo(vim, *args, **kwargs):
    '''Domain Name Server (DNS) Configuration Specification - a data object for
    reporting the configuration of RFC 1034 client side DNS settings.'''
    
    obj = vim.client.factory.create('ns0:NetDnsConfigInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'dhcp', 'domainName', 'hostName' ]
    optional = [ 'ipAddress', 'searchDomain', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    