# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFirewallRuleset(vim, *args, **kwargs):
    '''Data object that describes a single network ruleset that can be allowed or
    blocked by the firewall using the HostFirewallSystem object.'''
    
    obj = vim.client.factory.create('ns0:HostFirewallRuleset')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'key', 'label', 'required', 'rule', 'service' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    