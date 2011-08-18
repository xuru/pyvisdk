# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourceAllocationOption(vim, *args, **kwargs):
    '''The ResourceAllocationOption data object specifies value ranges and default
    values for ResourceAllocationInfo.'''
    
    obj = vim.client.factory.create('ns0:ResourceAllocationOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'sharesOption' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    