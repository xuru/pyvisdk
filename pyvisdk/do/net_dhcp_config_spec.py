# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetDhcpConfigSpec(vim, *args, **kwargs):
    '''Dynamic Host Configuration Protocol Configuration for IP version 4 and version
    6.'''
    
    obj = vim.client.factory.create('ns0:NetDhcpConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'ipv4', 'ipv6' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    