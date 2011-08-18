# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DynamicArray(vim, *args, **kwargs):
    '''DynamicArray is a data object type that represents an array of dynamically-
    typed objects. A client should only see a DynamicArray object when the element
    type is unknown (meaning the type is newer than the client). Otherwise, a
    client would see the type as T[] where T is known.'''
    
    obj = vim.client.factory.create('ns0:DynamicArray')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dynamicType', 'val' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    