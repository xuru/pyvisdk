# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TaskFilterSpecByUsername(vim, *args, **kwargs):
    '''This data object type enables you to filter task history according to the users
    who performed the tasks.'''
    
    obj = vim.client.factory.create('ns0:TaskFilterSpecByUsername')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'systemUser', 'userList' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    