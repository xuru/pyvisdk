# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ResourcePoolSummary(vim, *args, **kwargs):
    '''This data object type encapsulates a typical set of resource pool information
    that is useful for list views and summary pages.'''
    
    obj = vim.client.factory.create('ns0:ResourcePoolSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'config', 'configuredMemoryMB', 'name', 'quickStats', 'runtime' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    