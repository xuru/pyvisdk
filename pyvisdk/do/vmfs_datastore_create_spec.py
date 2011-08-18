# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreCreateSpec(vim, *args, **kwargs):
    '''This data object type is used when creating a new VMFS datastore, to create a
    specification for the VMFS datastore.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreCreateSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'diskUuid', 'extent', 'partition', 'vmfs' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    