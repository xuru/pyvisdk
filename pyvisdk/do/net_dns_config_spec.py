
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetDnsConfigSpec(vim, *args, **kwargs):
    '''Domain Name Server (DNS) Configuration Specification - a data object for
    configuring the RFC 1034 client side DNS settings. TBD: remove this section,
    only for discussing what goes into this object. Place properties here that are
    specific to the RFC/common to all systems. Properties that are platform
    specific should go into a separate config spec. http://technet.microsoft.com
    /en-us/library/cc778792.aspx http://en.wikipedia.org/wiki/Microsoft_DNS'''
    
    obj = vim.client.factory.create('ns0:NetDnsConfigSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'dhcp', 'domainName', 'hostName', 'ipAddress', 'searchDomain',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    