# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskRawDiskMappingVer1BackingOption(vim, *args, **kwargs):
    '''The VirtualDiskOption.RawDiskMappingVer1BackingOption object type contains the
    available options when backing a virtual disk using a raw device mapping on ESX
    Server 2.5 or 3.x.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskRawDiskMappingVer1BackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'type', 'autoDetectAvailable', 'compatibilityMode',
        'descriptorFileNameExtensions', 'diskMode', 'uuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    