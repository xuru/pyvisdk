# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineSnapshotTree(vim, *args, **kwargs):
    '''SnapshotTree encapsulates all the read-only data produced by the snapshot.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineSnapshotTree')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backupManifest', 'childSnapshotList', 'createTime', 'description', 'id',
        'name', 'quiesced', 'replaySupported', 'snapshot', 'state', 'vm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    