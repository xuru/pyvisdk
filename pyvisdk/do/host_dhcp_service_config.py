# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDhcpServiceConfig(vim, *args, **kwargs):
    '''This data object type describes the configuration of a DHCP service instance
    representing both the configured properties on the instance and identification
    information.'''
    
    obj = vim.client.factory.create('ns0:HostDhcpServiceConfig')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'changeOperation', 'key', 'spec' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    