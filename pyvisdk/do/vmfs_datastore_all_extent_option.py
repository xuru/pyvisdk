# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreAllExtentOption(vim, *args, **kwargs):
    '''Datastore addition policy to use the entire disk as a single extent for a VMFS
    datastore. If there is any data on the disk, it will be overwritten.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreAllExtentOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'layout', 'vmfsExtent' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    