# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PosixUserSearchResult(vim, *args, **kwargs):
    '''Searching for users and groups on POSIX systems provides User ID and Group ID
    information, in addition to that defined in UserSearchResult.'''
    
    obj = vim.client.factory.create('ns0:PosixUserSearchResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'fullName', 'group', 'principal', 'id', 'shellAccess' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    