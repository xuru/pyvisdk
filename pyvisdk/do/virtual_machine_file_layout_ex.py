# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineFileLayoutEx(vim, *args, **kwargs):
    '''Detailed description of files that make up a virtual machine on disk. The file
    layout is broken into 4 major sections:* Configuration: Files stored in the
    configuration directory * Log: Files stored in the log directory * Disk: Files
    stored relative to a disk configuration file * Snapshot: Stored in the snapshot
    directoryOften the same directory is used for configuration, log, disk and
    snapshots.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineFileLayoutEx')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'disk', 'file', 'snapshot', 'timestamp' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    