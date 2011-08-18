# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualCdromIsoBackingInfo(vim, *args, **kwargs):
    '''The VirtualCdrom.IsoBackingInfo data class represents an ISO backing for a
    virtual CD-ROM.'''
    
    obj = vim.client.factory.create('ns0:VirtualCdromIsoBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastore', 'fileName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    