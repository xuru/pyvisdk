# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ObjectUpdate(vim, *args, **kwargs):
    '''The ObjectUpdate data object type contains information about changes to a
    particular managed object. We distinguish updates when an object is created,
    destroyed, or modified, as well as when the object enters or leaves the set of
    objects dynamically associated with a filter.'''
    
    obj = vim.client.factory.create('ns0:ObjectUpdate')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'changeSet', 'kind', 'missingSet', 'obj' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    