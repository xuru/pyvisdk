# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CompositePolicyOption(vim, *args, **kwargs):
    '''DataObject represents a composite Policy that is created by the user using
    different PolicyOptions. The options set in the CompositePolicyOption should be
    derived from the possible options as indicated by the
    CompositePolicyOptionMetadata.'''
    
    obj = vim.client.factory.create('ns0:CompositePolicyOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'id', 'parameter', 'option' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    