# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualSwitchAutoBridge(vim, *args, **kwargs):
    '''This data type describes a bridge that automatically selects a particular
    physical network adapter on the host according to some predetermined policy.
    Used primarily to support mobility scenarios.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualSwitchAutoBridge')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'excludedNicDevice' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    