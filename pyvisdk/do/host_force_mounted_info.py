# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostForceMountedInfo(vim, *args, **kwargs):
    '''When the system detects a copy of a VmfsVolume, it will not be auto-mounted on
    the host and it will be detected as 'UnresolvedVmfsVolume'. If user decides to
    keep the original Uuid and mount it on the host, it will have 'forceMounted'
    flag and 'forceMountedInfo' set. 'ForceMountedInfo' provides additional
    information specific to user-mounted VmfsVolume.'''
    
    obj = vim.client.factory.create('ns0:HostForceMountedInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'mounted', 'persist' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    