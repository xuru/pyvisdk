# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DiskChangeInfo(vim, *args, **kwargs):
    '''Data structure to describe areas in a disk associated with this VM that have
    been modified since a well-defined point in the past. Returned by
    QueryChangedDiskAreas. This data structure describes a subset of the disk
    identified by startOffset and length. All areas that have been modified within
    this interval are listed under changedArea.'''
    
    obj = vim.client.factory.create('ns0:DiskChangeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'changedArea', 'length', 'startOffset' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    