# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PortGroupProfile(vim, *args, **kwargs):
    '''This data object type is a base class for the different kinds of port group
    profiles.'''
    
    obj = vim.client.factory.create('ns0:PortGroupProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'policy', 'key', 'name', 'networkPolicy', 'vlan', 'vswitch' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    