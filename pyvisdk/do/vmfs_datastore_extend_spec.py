# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreExtendSpec(vim, *args, **kwargs):
    '''Specification to increase the capacity of a VMFS datastore by adding one or
    more new extents to the datastore. All the extents to be added must be on the
    same disk. Extension is different from creation in that the VMFS creation
    specification need not be specified.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreExtendSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'diskUuid', 'extent', 'partition' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    