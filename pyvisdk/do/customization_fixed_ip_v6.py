# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationFixedIpV6(vim, *args, **kwargs):
    '''Use a static ipv6 address for the virtual network adapter'''
    
    obj = vim.client.factory.create('ns0:CustomizationFixedIpV6')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'ipAddress', 'subnetMask' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    