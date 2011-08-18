# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDrsVmConfigInfo(vim, *args, **kwargs):
    '''DRS configuration for a single virtual machine. This makes it possible to
    override the default behavior for an individual virtual machine.'''
    
    obj = vim.client.factory.create('ns0:ClusterDrsVmConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'behavior', 'enabled', 'key' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    