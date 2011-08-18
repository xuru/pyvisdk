# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ProductComponentInfo(vim, *args, **kwargs):
    '''ProductComponentInfo data object type describes installed components. Product
    component is defined as a software module that is released and versioned
    independently but has dependency relationship with other products. If one
    product, for usability or any other reason, bundles other products,
    ProductComponentInfo type may be used to describe installed components. For
    example, ESX product may bundle VI Client in its releases.'''
    
    obj = vim.client.factory.create('ns0:ProductComponentInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'id', 'name', 'release', 'version' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    