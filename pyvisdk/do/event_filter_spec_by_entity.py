# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventFilterSpecByEntity(vim, *args, **kwargs):
    '''This option specifies a managed entity used to filter event history. If the
    specified managed entity is a Folder or a ResourcePool, the query will actually
    be performed on the entities contained within that Folder or ResourcePool, so
    you cannot query for events on Folders and ResourcePools themselves this way.'''
    
    obj = vim.client.factory.create('ns0:EventFilterSpecByEntity')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'entity', 'recursion' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    