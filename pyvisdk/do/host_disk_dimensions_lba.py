# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskDimensionsLba(vim, *args, **kwargs):
    '''This data object type describes the logical block addressing system that uses
    block numbers and block sizes to refer to a block. This scheme is employed by
    SCSI. If a SCSI disk is not involved, then blockSize is 512 bytes.'''
    
    obj = vim.client.factory.create('ns0:HostDiskDimensionsLba')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'block', 'blockSize' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    