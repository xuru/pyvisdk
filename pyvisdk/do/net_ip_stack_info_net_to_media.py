# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetIpStackInfoNetToMedia(vim, *args, **kwargs):
    '''Information from an IP stack about known mappings betwwen an IP address and the
    underlying physical address it maps to as learned by: IPv4: Address Resolution
    Protocol (ARP) RFC 826 IPv6: Neighbor Discovery Protocol (NDP) RFC 4861'''
    
    obj = vim.client.factory.create('ns0:NetIpStackInfoNetToMedia')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'device', 'ipAddress', 'physicalAddress', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    