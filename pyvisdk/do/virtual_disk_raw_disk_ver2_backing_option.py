# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskRawDiskVer2BackingOption(vim, *args, **kwargs):
    '''The VirtualDiskOption.RawDiskVer2BackingOption object type contains the
    available options when backing a virtual disk using a host device on VMware
    Server.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskRawDiskVer2BackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable', 'descriptorFileNameExtensions', 'uuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    