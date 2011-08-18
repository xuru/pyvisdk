# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreSpec(vim, *args, **kwargs):
    '''Base class for VMFS datastore addition specification. Used as a generic way to
    point to one of the creation specifications that can be used to apply a
    specification to effect the creation or extension of a VMFS datastore.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'diskUuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    