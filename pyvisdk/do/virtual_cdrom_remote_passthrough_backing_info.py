# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdromRemotePassthroughBackingInfo(vim, *args, **kwargs):
    '''The VirtualCdrom.RemotePassthroughBackingInfo data object type contains the
    information to specify a remote pass-through device backing of a virtual CD-
    ROM.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdromRemotePassthroughBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect', 'exclusive' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    