# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def MissingObject(vim, *args, **kwargs):
    '''Used for reporting missing objects that were explicitly referenced by a filter
    spec. In other words, any of the objects referenced in objectSet'''
    
    obj = vim.client.factory.create('ns0:MissingObject')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'fault', 'obj' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    