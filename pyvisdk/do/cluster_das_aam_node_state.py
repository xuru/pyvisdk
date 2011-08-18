# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasAamNodeState(vim, *args, **kwargs):
    '''The ClusterDasAamNodeState data object represents the state of the HA service
    on an ESX host. (AAM is a component of this service.)'''
    
    obj = vim.client.factory.create('ns0:ClusterDasAamNodeState')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configState', 'host', 'name', 'runtimeState' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    