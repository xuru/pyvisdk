# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetIpRouteConfigInfoIpRoute(vim, *args, **kwargs):
    '''IpRoute report an individual host, network or default destination network
    reachable through a given gateway.'''
    
    obj = vim.client.factory.create('ns0:NetIpRouteConfigInfoIpRoute')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'gateway', 'network', 'prefixLength' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    