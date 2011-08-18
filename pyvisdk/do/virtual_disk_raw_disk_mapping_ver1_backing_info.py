# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskRawDiskMappingVer1BackingInfo(vim, *args, **kwargs):
    '''This data object type contains information about backing a virtual disk using a
    raw device mapping. Supported for ESX Server 2.5 and 3.x.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskRawDiskMappingVer1BackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastore', 'fileName', 'changeId', 'compatibilityMode', 'contentId',
        'deviceName', 'diskMode', 'lunUuid', 'parent', 'uuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    