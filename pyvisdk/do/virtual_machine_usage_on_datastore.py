# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineUsageOnDatastore(vim, *args, **kwargs):
    '''Storage space used by this virtual machine on a particular datastore.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineUsageOnDatastore')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'committed', 'datastore', 'uncommitted', 'unshared' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    