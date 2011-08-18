# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dhcp', 'domainName', 'hostName', 'ipAddress', 'searchDomain' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    