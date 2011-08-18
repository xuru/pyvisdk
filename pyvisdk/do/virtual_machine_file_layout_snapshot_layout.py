# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineFileLayoutSnapshotLayout(vim, *args, **kwargs):
    '''Enumerates the set of files that make up a snapshot or redo-point'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineFileLayoutSnapshotLayout')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'key', 'snapshotFile' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    