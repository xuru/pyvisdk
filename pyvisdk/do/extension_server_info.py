# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ExtensionServerInfo(vim, *args, **kwargs):
    '''This data object type describes a server for the extension.'''
    
    obj = vim.client.factory.create('ns0:ExtensionServerInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'adminEmail', 'company', 'description', 'serverThumbprint', 'type', 'url' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    