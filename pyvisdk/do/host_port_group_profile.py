# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPortGroupProfile(vim, *args, **kwargs):
    '''This data object type represents the profile for a Port Group that will be used
    by ESX host.'''
    
    obj = vim.client.factory.create('ns0:HostPortGroupProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'policy', 'key', 'name', 'networkPolicy', 'vlan', 'vswitch',
        'ipConfig' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    