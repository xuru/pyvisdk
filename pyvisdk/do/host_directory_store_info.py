# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDirectoryStoreInfo(vim, *args, **kwargs):
    '''HostDirectoryStoreInfo is a base class for objects that provide information
    about directory-based authentication stores.'''
    
    obj = vim.client.factory.create('ns0:HostDirectoryStoreInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    