# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreSummary(vim, *args, **kwargs):
    '''Summary information about the datastore. The status fields and managed object
    reference is not set when an object of this type is created. These fields and
    references are typically set later when these objects are associated with a
    host.'''
    
    obj = vim.client.factory.create('ns0:DatastoreSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'accessible', 'capacity', 'datastore', 'freeSpace', 'multipleHostAccess',
        'name', 'type', 'uncommitted', 'url' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    