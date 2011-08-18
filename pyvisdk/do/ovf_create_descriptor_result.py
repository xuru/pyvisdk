# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfCreateDescriptorResult(vim, *args, **kwargs):
    '''The result of creating the OVF descriptor for the entity.'''
    
    obj = vim.client.factory.create('ns0:OvfCreateDescriptorResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'error', 'includeImageFiles', 'ovfDescriptor', 'warning' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    