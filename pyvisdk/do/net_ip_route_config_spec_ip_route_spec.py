# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetIpRouteConfigSpecIpRouteSpec(vim, *args, **kwargs):
    '''Specify an individual host, network or default destination network reachable
    through a given gateway.'''
    
    obj = vim.client.factory.create('ns0:NetIpRouteConfigSpecIpRouteSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'gateway', 'network', 'operation', 'prefixLength' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    