# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def SessionManagerLocalTicket(vim, *args, **kwargs):
    '''This data object type contains the user name and location of the file
    containing the password that clients can use for one-time logon to a server.'''
    
    obj = vim.client.factory.create('ns0:SessionManagerLocalTicket')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'passwordFilePath', 'userName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    