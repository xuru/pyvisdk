# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostProfileHostBasedConfigSpec(vim, *args, **kwargs):
    '''DataObject which defines the configSpec when HostProfile is being created or
    updated from a Host.'''
    
    obj = vim.client.factory.create('ns0:HostProfileHostBasedConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'annotation', 'enabled', 'name', 'host' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    