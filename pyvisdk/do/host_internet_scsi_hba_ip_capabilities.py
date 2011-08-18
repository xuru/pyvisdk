# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaIPCapabilities(vim, *args, **kwargs):
    '''The IP Capabilities for the host bus adapter'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaIPCapabilities')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'addressSettable', 'alternateDnsServerAddressSettable', 'arpRedirectSettable',
        'defaultGatewaySettable', 'hostNameAsTargetAddress',
        'ipConfigurationMethodSettable', 'ipv6Supported', 'mtuSettable',
        'nameAliasSettable', 'primaryDnsServerAddressSettable', 'subnetMaskSettable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    