# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineStorageSummary(vim, *args, **kwargs):
    '''A subset of the storage information of this virtual machine.See
    VirtualMachineStorageInfo for a detailed storage break-up.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineStorageSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'committed', 'timestamp', 'uncommitted', 'unshared' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    