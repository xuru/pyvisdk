# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ExtensionClientInfo(vim, *args, **kwargs):
    '''This data object type describes a client of the extension.'''
    
    obj = vim.client.factory.create('ns0:ExtensionClientInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'company', 'description', 'type', 'url', 'version' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    