# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfoLogicalUnitStorageArrayTypePolicy(vim, *args, **kwargs):
    '''This data object type describes a storage array type policy for for a device.
    This policy determines how device I/O and management is performed.'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfoLogicalUnitStorageArrayTypePolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'policy' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    