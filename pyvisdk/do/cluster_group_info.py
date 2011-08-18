# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterGroupInfo(vim, *args, **kwargs):
    '''ClusterGroupInfo is the base type for all virtual machine and host groups. All
    virtual machines and hosts that are part of a group must be part of the same
    cluster.'''
    
    obj = vim.client.factory.create('ns0:ClusterGroupInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    