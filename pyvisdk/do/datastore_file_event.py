# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreFileEvent(vim, *args, **kwargs):
    '''Base class for events related to datastore file and directory
    operations.Property inherited from DatastoreEvent refers to the destination
    datastore in case there is more than datastore involved in the operation.'''
    
    obj = vim.client.factory.create('ns0:DatastoreFileEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'datastore', 'targetFile' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    