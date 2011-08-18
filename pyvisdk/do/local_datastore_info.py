# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def LocalDatastoreInfo(vim, *args, **kwargs):
    '''The information details about a datastore that is local to a host.'''
    
    obj = vim.client.factory.create('ns0:LocalDatastoreInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'freeSpace', 'maxFileSize', 'name', 'timestamp', 'url', 'path' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    