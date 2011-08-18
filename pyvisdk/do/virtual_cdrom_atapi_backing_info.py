# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdromAtapiBackingInfo(vim, *args, **kwargs):
    '''The VirtualCdrom.AtapiBackingInfo data object type represents an ATAPI device
    backing for a virtual CD-ROM.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdromAtapiBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    