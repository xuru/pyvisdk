# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterHostRecommendation(vim, *args, **kwargs):
    '''A DRS recommended host for either powering on, resuming or reverting a virtual
    machine, or migrating a virtual machine from outside the cluster.'''
    
    obj = vim.client.factory.create('ns0:ClusterHostRecommendation')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'host', 'rating' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    