# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostParallelScsiHba(vim, *args, **kwargs):
    '''The ParallelScsiHba data object type describes a parallel SCSI host bus
    adapter.'''
    
    obj = vim.client.factory.create('ns0:HostParallelScsiHba')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bus', 'device', 'driver', 'key', 'model', 'pci', 'status' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    