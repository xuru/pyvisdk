# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNatServicePortForwardSpec(vim, *args, **kwargs):
    '''This data object type describes the Network Address Translation (NAT) port
    forwarding specification.'''
    
    obj = vim.client.factory.create('ns0:HostNatServicePortForwardSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'guestIpAddress', 'guestPort', 'hostPort', 'name', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    