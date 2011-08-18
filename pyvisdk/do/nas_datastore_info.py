# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NasDatastoreInfo(vim, *args, **kwargs):
    '''Information details about a network-attached storage (NAS) datastore.'''
    
    obj = vim.client.factory.create('ns0:NasDatastoreInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'freeSpace', 'maxFileSize', 'name', 'timestamp', 'url', 'nas' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    