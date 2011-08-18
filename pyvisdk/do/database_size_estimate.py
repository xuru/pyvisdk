# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatabaseSizeEstimate(vim, *args, **kwargs):
    '''DatabaseSizeEstimate contains information about the size required to by the
    database.'''
    
    obj = vim.client.factory.create('ns0:DatabaseSizeEstimate')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'size' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    