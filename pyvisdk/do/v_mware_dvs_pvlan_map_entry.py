# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareDVSPvlanMapEntry(vim, *args, **kwargs):
    '''The class represents a PVLAN id.'''
    
    obj = vim.client.factory.create('ns0:VMwareDVSPvlanMapEntry')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'primaryVlanId', 'pvlanType', 'secondaryVlanId' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    