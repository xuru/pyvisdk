# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkInfo(vim, *args, **kwargs):
    '''This data object type describes networking host configuration data objects.'''
    
    obj = vim.client.factory.create('ns0:HostNetworkInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'atBootIpV6Enabled', 'consoleIpRouteConfig', 'consoleVnic', 'dhcp',
        'dnsConfig', 'ipRouteConfig', 'ipV6Enabled', 'nat', 'pnic', 'portgroup',
        'proxySwitch', 'routeTableInfo', 'vnic', 'vswitch' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    