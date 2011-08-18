# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreSingleExtentOption(vim, *args, **kwargs):
    '''Datastore addition policy to use a single extent on the disk for a VMFS
    datastore. A single extent implies that one disk partition will be created on
    the disk for creating or increasing the capacity of a VMFS datastore.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreSingleExtentOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'layout', 'vmfsExtent' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    