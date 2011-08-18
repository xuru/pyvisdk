# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def UserSession(vim, *args, **kwargs):
    '''Information about a current user session.'''
    
    obj = vim.client.factory.create('ns0:UserSession')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'fullName', 'key', 'lastActiveTime', 'locale', 'loginTime', 'messageLocale',
        'userName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    