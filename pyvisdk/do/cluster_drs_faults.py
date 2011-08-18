# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDrsFaults(vim, *args, **kwargs):
    '''The faults generated by DRS when it tries to make recommendations for rule
    enforcement, power management, etc., and indexed in a tree structure with
    reason for recommendations and VM to migrate (optional) as the index keys.'''
    
    obj = vim.client.factory.create('ns0:ClusterDrsFaults')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'faultsByVm', 'reason' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    