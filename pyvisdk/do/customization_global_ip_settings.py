# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationGlobalIPSettings(vim, *args, **kwargs):
    '''A collection of global IP settings for a virtual network adapter. In Linux, DNS
    server settings are global. The settings can either be statically set or
    supplied by a DHCP server.'''
    
    obj = vim.client.factory.create('ns0:CustomizationGlobalIPSettings')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dnsServerList', 'dnsSuffixList' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    