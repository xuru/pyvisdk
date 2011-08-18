# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreExpandSpec(vim, *args, **kwargs):
    '''Specification to increase the capacity of a VMFS datastore by expanding
    (increasing the size of) an existing extent of the datastore.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreExpandSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'diskUuid', 'extent', 'partition' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    