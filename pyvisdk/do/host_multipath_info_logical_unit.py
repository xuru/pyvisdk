# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfoLogicalUnit(vim, *args, **kwargs):
    '''This data object type represents a storage entity that provides disk blocks to
    a host.'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfoLogicalUnit')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'id', 'key', 'lun', 'path', 'policy', 'storageArrayTypePolicy' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    