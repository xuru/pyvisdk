# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostIpRouteEntry(vim, *args, **kwargs):
    '''IpRouteEntry. Routing entries are individual static routes which combined with
    the default route form all of the routing rules for a host.'''
    
    obj = vim.client.factory.create('ns0:HostIpRouteEntry')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'gateway', 'network', 'prefixLength' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    