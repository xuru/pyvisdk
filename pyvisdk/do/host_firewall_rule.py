# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFirewallRule(vim, *args, **kwargs):
    '''This data object type describes a port (or range of ports), identified by port
    number(s), direction and protocol. It is used as a convenient way for users to
    express what ports they want to permit through the firewall.'''
    
    obj = vim.client.factory.create('ns0:HostFirewallRule')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'direction', 'endPort', 'port', 'protocol' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    