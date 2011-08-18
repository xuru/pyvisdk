# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StorageIORMConfigSpec(vim, *args, **kwargs):
    '''Configuration settings used for creating or reconfiguring storage I/O resource
    management.All fields are defined as optional. If a field is unset, the
    property is not changed.'''
    
    obj = vim.client.factory.create('ns0:StorageIORMConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'congestionThreshold', 'enabled' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    