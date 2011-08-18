# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskPartitionedRawDiskVer2BackingOption(vim, *args, **kwargs):
    '''The VirtualDiskOption.PartitionedRawDiskVer2BackingOption object type contains
    the available options when backing a virtual disk using one or more partitions
    on a physical disk device. This backing is supported in VMware Server.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskPartitionedRawDiskVer2BackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable', 'descriptorFileNameExtensions', 'uuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    