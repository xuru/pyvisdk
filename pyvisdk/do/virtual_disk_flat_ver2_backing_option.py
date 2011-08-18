# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskFlatVer2BackingOption(vim, *args, **kwargs):
    '''This data object type contains the available options when backing a virtual
    disk using a host file with the flat file format used in VMware Server and in
    ESX Server 2.x and greater. Flat disks are pre-allocated, whereas sparse disks
    are grown as needed.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskFlatVer2BackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'fileNameExtensions', 'diskMode', 'eagerlyScrub', 'growable',
        'hotGrowable', 'split', 'thinProvisioned', 'uuid', 'writeThrough' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    