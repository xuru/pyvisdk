# -*- coding: ascii -*-

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
        
    signature = [ 'dhcp', 'domainName', 'hostName' ]
    inherited = [ 'ipAddress', 'searchDomain' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    