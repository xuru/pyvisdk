# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskFlatVer1BackingInfo(vim, *args, **kwargs):
    '''This data object type contains information about backing a virtual disk by
    using a virtual disk file on the host, in the flat file format used by GSX
    Server 2.x.Flat disks are allocated when created, unlike sparse disks, which
    grow as needed.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskFlatVer1BackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastore', 'fileName', 'contentId', 'diskMode', 'parent', 'split',
        'writeThrough' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    