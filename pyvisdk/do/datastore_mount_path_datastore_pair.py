# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreMountPathDatastorePair(vim, *args, **kwargs):
    '''Contains a mapping of an old mount path and its corresponding resignatured or
    remounted datastore'''
    
    obj = vim.client.factory.create('ns0:DatastoreMountPathDatastorePair')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastore', 'oldMountPath' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    