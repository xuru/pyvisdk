# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNasVolume(vim, *args, **kwargs):
    '''This data object type describes the NAS volume. Applies to both NFS and CIFS.'''
    
    obj = vim.client.factory.create('ns0:HostNasVolume')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'capacity', 'name', 'type', 'remoteHost', 'remotePath', 'userName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    