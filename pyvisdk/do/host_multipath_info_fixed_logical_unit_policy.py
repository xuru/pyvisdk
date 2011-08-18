# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfoFixedLogicalUnitPolicy(vim, *args, **kwargs):
    '''This data object type describes a multipathing policy for a logical unit which
    uses a preferred path whenever possible.'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfoFixedLogicalUnitPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'policy', 'prefer' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    