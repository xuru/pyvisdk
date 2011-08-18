# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourceConfigOption(vim, *args, **kwargs):
    '''This data object type is a default value and value range specification for
    ResourceConfigSpec object.'''
    
    obj = vim.client.factory.create('ns0:ResourceConfigOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cpuAllocationOption', 'memoryAllocationOption' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    