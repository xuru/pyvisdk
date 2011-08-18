# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ModeInfo(vim, *args, **kwargs):
    '''The FileAccess.Modes data object type defines the known access modes for a
    datastore. The property values specify how to interpret the "what" property for
    a FileAccess object.'''
    
    obj = vim.client.factory.create('ns0:ModeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'admin', 'browse', 'full', 'modify', 'read', 'use' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    