# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkTrafficShapingPolicy(vim, *args, **kwargs):
    '''This data object type describes traffic shaping policy.'''
    
    obj = vim.client.factory.create('ns0:HostNetworkTrafficShapingPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'averageBandwidth', 'burstSize', 'enabled', 'peakBandwidth' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    