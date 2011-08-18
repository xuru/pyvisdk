# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfoPath(vim, *args, **kwargs):
    '''Path is a storage entity that represents a topological path from a host bus
    adapter to a SCSI logical unit. Each path is unique although each host bus
    adapter/SCSI logical unit pair can have multiple paths.Path objects are
    identified by a key. The specifics of how the key is formatted are dependent on
    the implementation. Example implementations include using strings like
    "vmhba1:0:0:0".'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfoPath')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'adapter', 'isWorkingPath', 'key', 'lun', 'name', 'pathState', 'state',
        'transport' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    