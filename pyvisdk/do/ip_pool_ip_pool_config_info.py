# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dhcpServerAvailable', 'dns', 'gateway', 'ipPoolEnabled', 'netmask', 'range',
        'subnetAddress' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    