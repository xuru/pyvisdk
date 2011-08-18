# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def IpPool(vim, *args, **kwargs):
    '''Specifications of the network configuration to be used on a network. This is
    used to generate IP addresses and for self-customization of vApps.'''
    
    obj = vim.client.factory.create('ns0:IpPool')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dnsDomain', 'dnsSearchPath', 'hostPrefix', 'httpProxy', 'id', 'ipv4Config',
        'ipv6Config', 'name', 'networkAssociation' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    