# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PropertyFilterUpdate(vim, *args, **kwargs):
    '''The PropertyFilterUpdate data object type contains a list of updates to data
    visible through a specific filter. Note that if a property changes through
    multiple filters, then a client receives an update for each filter.'''
    
    obj = vim.client.factory.create('ns0:PropertyFilterUpdate')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'filter', 'missingSet', 'objectSet' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    