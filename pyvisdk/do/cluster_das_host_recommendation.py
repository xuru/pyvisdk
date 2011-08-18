# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasHostRecommendation(vim, *args, **kwargs):
    '''A host recommendation for a virtual machine managed by the VMware HA Service.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasHostRecommendation')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'drsRating', 'host' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    