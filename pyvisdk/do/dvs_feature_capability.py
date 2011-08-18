# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSFeatureCapability(vim, *args, **kwargs):
    '''Dataobject representing the feature capabilities supported by the vNetwork
    Distributed Virtual Switch.'''
    
    obj = vim.client.factory.create('ns0:DVSFeatureCapability')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'networkResourceManagementSupported', 'networkResourcePoolHighShareValue',
        'nicTeamingPolicy', 'vmDirectPathGen2Supported' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    