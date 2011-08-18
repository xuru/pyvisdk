# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AuthorizationRole(vim, *args, **kwargs):
    '''This data object type specifies a collection of privileges used to grant access
    to users on managed entities.'''
    
    obj = vim.client.factory.create('ns0:AuthorizationRole')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'info', 'name', 'privilege', 'roleId', 'system' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    