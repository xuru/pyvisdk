# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dhcp', 'domainName', 'hostName', 'ipAddress', 'searchDomain' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    