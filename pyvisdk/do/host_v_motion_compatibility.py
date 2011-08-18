# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVMotionCompatibility(vim, *args, **kwargs):
    '''The object type for the array returned by queryVMotionCompatibility; specifies
    the VMotion compatibility types for a host.'''
    
    obj = vim.client.factory.create('ns0:HostVMotionCompatibility')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'compatibility', 'host' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    