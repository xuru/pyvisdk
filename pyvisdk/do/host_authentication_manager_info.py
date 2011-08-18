# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostAuthenticationManagerInfo(vim, *args, **kwargs):
    '''The HostAuthenticationManagerInfo data object provides access to authentication
    information for the ESX host.'''
    
    obj = vim.client.factory.create('ns0:HostAuthenticationManagerInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'authConfig' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    