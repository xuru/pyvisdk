
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationGlobalIPSettings(vim, *args, **kwargs):
    '''A collection of global IP settings for a virtual network adapter. In Linux, DNS
    server settings are global. The settings can either be statically set or
    supplied by a DHCP server.'''
    
    obj = vim.client.factory.create('ns0:CustomizationGlobalIPSettings')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'dnsServerList', 'dnsSuffixList', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    