# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreMultipleExtentOption(vim, *args, **kwargs):
    '''Datastore addition policy to use multiple extents on the disk for a VMFS
    datastore. Multiple extents implies that more than one disk partition will be
    created on the disk for creating or increasing the capacity of a VMFS
    datastore. Multiple extents are needed when unpartitioned space is fragmented
    in the existing partition layout of the disk.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreMultipleExtentOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'layout', 'vmfsExtent' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    