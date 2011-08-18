# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def IsoImageFileInfo(vim, *args, **kwargs):
    '''This data object type describes a file that is an ISO CD-ROM image.'''
    
    obj = vim.client.factory.create('ns0:IsoImageFileInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'fileSize', 'modification', 'owner', 'path' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    