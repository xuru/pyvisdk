# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetDhcpConfigInfoDhcpOptions(vim, *args, **kwargs):
    '''Provides for reporting of DHCP client. This data object may be used at a per
    interface or per system scope.'''
    
    obj = vim.client.factory.create('ns0:NetDhcpConfigInfoDhcpOptions')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'config', 'enable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    