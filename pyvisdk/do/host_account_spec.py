# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostAccountSpec(vim, *args, **kwargs):
    '''This data object type contains common parameters for local account creation.
    The password and description properties are not supported for group accounts on
    POSIX hosts.'''
    
    obj = vim.client.factory.create('ns0:HostAccountSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'description', 'id', 'password' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    