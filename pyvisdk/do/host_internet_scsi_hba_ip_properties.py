# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaIPProperties(vim, *args, **kwargs):
    '''The IP properties for the host bus adapter'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaIPProperties')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'address', 'alternateDnsServerAddress', 'arpRedirectEnabled', 'defaultGateway',
        'dhcpConfigurationEnabled', 'ipv6Address', 'ipv6DefaultGateway',
        'ipv6SubnetMask', 'jumboFramesEnabled', 'mac', 'mtu',
        'primaryDnsServerAddress', 'subnetMask' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    