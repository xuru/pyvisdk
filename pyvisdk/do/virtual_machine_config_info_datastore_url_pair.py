# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigInfoDatastoreUrlPair(vim, *args, **kwargs):
    '''Contains the name of a datastore, and its local file path on the host currently
    affiliated with this virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigInfoDatastoreUrlPair')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name', 'url' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    