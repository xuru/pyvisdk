# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationIPSettings(vim, *args, **kwargs):
    '''IP settings for a virtual network adapter.'''
    
    obj = vim.client.factory.create('ns0:CustomizationIPSettings')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dnsDomain', 'dnsServerList', 'gateway', 'ip', 'ipV6Spec', 'netBIOS',
        'primaryWINS', 'secondaryWINS', 'subnetMask' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    