# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DiagnosticManagerLogDescriptor(vim, *args, **kwargs):
    '''Describes a log file that is available on a server.'''
    
    obj = vim.client.factory.create('ns0:DiagnosticManagerLogDescriptor')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'creator', 'fileName', 'format', 'info', 'key', 'mimeType' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    