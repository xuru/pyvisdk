# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfCreateDescriptorParams(vim, *args, **kwargs):
    '''Collection of parameters for createDescriptor'''
    
    obj = vim.client.factory.create('ns0:OvfCreateDescriptorParams')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'description', 'includeImageFiles', 'name', 'ovfFiles' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    