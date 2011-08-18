# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskSparseVer1BackingOption(vim, *args, **kwargs):
    '''This data object type contains the available options when backing a virtual
    disk using a host file with the sparse file format from GSX Server 2.x.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskSparseVer1BackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'fileNameExtensions', 'diskModes', 'growable', 'split', 'writeThrough' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    