# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPatchManagerResult(vim, *args, **kwargs):
    '''The result of the operation. Some of the fields are only valid for specific
    operations.'''
    
    obj = vim.client.factory.create('ns0:HostPatchManagerResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'status', 'version', 'xmlResult' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    