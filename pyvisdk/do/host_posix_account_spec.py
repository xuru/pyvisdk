# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPosixAccountSpec(vim, *args, **kwargs):
    '''This data object type contains a POSIX-specific parameter for local account
    creation.'''
    
    obj = vim.client.factory.create('ns0:HostPosixAccountSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'description', 'id', 'password', 'posixId', 'shellAccess' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    