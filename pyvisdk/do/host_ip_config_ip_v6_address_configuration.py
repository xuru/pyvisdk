# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostIpConfigIpV6AddressConfiguration(vim, *args, **kwargs):
    '''The ipv6 address configuration'''
    
    obj = vim.client.factory.create('ns0:HostIpConfigIpV6AddressConfiguration')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoConfigurationEnabled', 'dhcpV6Enabled', 'ipV6Address' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    