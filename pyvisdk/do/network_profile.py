# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetworkProfile(vim, *args, **kwargs):
    '''DataObject represents a profile for network configuration.'''
    
    obj = vim.client.factory.create('ns0:NetworkProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'policy', 'consoleIpRouteConfig', 'dnsConfig', 'dvsHostNic',
        'dvsServiceConsoleNic', 'dvswitch', 'hostPortGroup', 'ipRouteConfig', 'pnic',
        'serviceConsolePortGroup', 'vmPortGroup', 'vswitch' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    