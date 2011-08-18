# -*- coding: ascii -*-

import logging

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
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'address', 'dhcp', 'domainName', 'hostName', 'searchDomain', 'virtualNicDevice' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    