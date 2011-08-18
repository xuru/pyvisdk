# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterRecommendation(vim, *args, **kwargs):
    '''Recommendation is the base class for any packaged group of actions that are
    intended to take the system from one state to another one.'''
    
    obj = vim.client.factory.create('ns0:ClusterRecommendation')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'action', 'key', 'prerequisite', 'rating', 'reason', 'reasonText', 'target',
        'time', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    