# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetIpConfigInfo(vim, *args, **kwargs):
    '''Protocol version independent address reporting data object for network
    interfaces.'''
    
    obj = vim.client.factory.create('ns0:NetIpConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoConfigurationEnabled', 'dhcp', 'ipAddress' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    