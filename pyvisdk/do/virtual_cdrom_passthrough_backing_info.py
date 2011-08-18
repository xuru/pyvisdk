# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdromPassthroughBackingInfo(vim, *args, **kwargs):
    '''The VirtualCdrom.PassthroughBackingInfo data class represents a device pass-
    through backing for a virtual CD-ROM.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdromPassthroughBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect', 'exclusive' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    