# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkConfig(vim, *args, **kwargs):
    '''This data object type describes networking host configuration data objects.
    These objects contain only the configuration information for networking. The
    runtime information is available from the NetworkInfo data object type. See
    HostNetworkInfo'''
    
    obj = vim.client.factory.create('ns0:HostNetworkConfig')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'consoleIpRouteConfig', 'consoleVnic', 'dhcp', 'dnsConfig', 'ipRouteConfig',
        'ipV6Enabled', 'nat', 'pnic', 'portgroup', 'proxySwitch', 'routeTableConfig',
        'vnic', 'vswitch' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    