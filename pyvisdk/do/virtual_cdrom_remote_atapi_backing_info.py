# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdromRemoteAtapiBackingInfo(vim, *args, **kwargs):
    '''The VirtualCdrom.RemoteAtapiBackingInfo data class represents a remote ATAPI
    device backing for a virtual CD-ROM.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdromRemoteAtapiBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    