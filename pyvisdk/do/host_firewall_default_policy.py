# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFirewallDefaultPolicy(vim, *args, **kwargs):
    '''Default settings for the firewall, used for ports that are not explicitly
    opened.'''
    
    obj = vim.client.factory.create('ns0:HostFirewallDefaultPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'incomingBlocked', 'outgoingBlocked' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    