# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfResourceMap(vim, *args, **kwargs):
    '''Maps source child entities to destination resource pools and resource settings.
    If a mapping is not specified, a child is copied as a direct child of the
    parent.'''
    
    obj = vim.client.factory.create('ns0:OvfResourceMap')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastore', 'parent', 'resourceSpec', 'source' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    