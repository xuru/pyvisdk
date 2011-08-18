# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDpmHostConfigInfo(vim, *args, **kwargs):
    '''DPM configuration for a single host. This makes it possible to override the
    default behavior for an individual host.'''
    
    obj = vim.client.factory.create('ns0:ClusterDpmHostConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'behavior', 'enabled', 'key' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    