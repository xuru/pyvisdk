# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineDatastoreInfo(vim, *args, **kwargs):
    '''DatastoreInfo describes a datastore that a virtual disk can be stored on.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineDatastoreInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configurationTag', 'name', 'capability', 'datastore', 'maxFileSize', 'mode' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    