# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaTargetSet(vim, *args, **kwargs):
    '''A collection of one or more static targets or discovery addresses. At least one
    of the arrays must be non-empty.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaTargetSet')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'sendTargets', 'staticTargets' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    