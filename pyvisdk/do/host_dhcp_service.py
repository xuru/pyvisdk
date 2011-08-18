# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDhcpService(vim, *args, **kwargs):
    '''A dynamic host control protocol (DHCP) service instance serves IP addresses to
    a single virtual network subnet. The instances may be handled collectively by a
    single server. This decision can be made during implementation.'''
    
    obj = vim.client.factory.create('ns0:HostDhcpService')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'key', 'spec' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    