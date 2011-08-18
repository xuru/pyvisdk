# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TraversalSpec(vim, *args, **kwargs):
    '''The TraversalSpec data object type specifies how to derive a new set of objects
    to add to the filter.It specifies a property path whose value is either another
    managed object or an array of managed objects included in the set of objects
    for consideration. This data object can also be named, using the "name" field
    in the base type.'''
    
    obj = vim.client.factory.create('ns0:TraversalSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name', 'path', 'selectSet', 'skip', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    