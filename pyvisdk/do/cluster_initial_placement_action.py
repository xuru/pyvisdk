# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterInitialPlacementAction(vim, *args, **kwargs):
    '''Describes an initial placement of a single virtual machine'''
    
    obj = vim.client.factory.create('ns0:ClusterInitialPlacementAction')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'target', 'type', 'pool', 'targetHost' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    