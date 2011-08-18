# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasAdvancedRuntimeInfo(vim, *args, **kwargs):
    '''Base class for advanced runtime information related to the high availability
    service for a cluster.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasAdvancedRuntimeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dasHostInfo' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    