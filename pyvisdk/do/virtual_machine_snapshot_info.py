# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineSnapshotInfo(vim, *args, **kwargs):
    '''The SnapshotInfo data object type provides all the information about the
    hierarchy of snapshots in a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineSnapshotInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'currentSnapshot', 'rootSnapshotList' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    