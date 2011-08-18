# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def Permission(vim, *args, **kwargs):
    '''This data object type provides assignment of some role access to a principal on
    a specific entity. A ManagedEntity is limited to one permission per principal.'''
    
    obj = vim.client.factory.create('ns0:Permission')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'entity', 'group', 'principal', 'propagate', 'roleId' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    