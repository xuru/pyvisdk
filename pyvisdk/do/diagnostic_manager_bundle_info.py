# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DiagnosticManagerBundleInfo(vim, *args, **kwargs):
    '''Describes a location of a diagnostic bundle and the server to which it belongs.
    This is a return type for the generateLogBundles operation.'''
    
    obj = vim.client.factory.create('ns0:DiagnosticManagerBundleInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'system', 'url' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    