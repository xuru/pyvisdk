# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskRawDiskVer2BackingInfo(vim, *args, **kwargs):
    '''This data object type contains information about backing a virtual disk by
    using a host device, as used by VMware Server.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskRawDiskVer2BackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect', 'changeId', 'descriptorFileName', 'uuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    