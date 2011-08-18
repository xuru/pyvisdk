# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostActiveDirectorySpec(vim, *args, **kwargs):
    '''The HostActiveDirectorySpec data object defines properties for Active Directory
    domain access.'''
    
    obj = vim.client.factory.create('ns0:HostActiveDirectorySpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'domainName', 'password', 'userName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    