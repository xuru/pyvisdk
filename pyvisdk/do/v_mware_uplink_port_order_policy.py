# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareUplinkPortOrderPolicy(vim, *args, **kwargs):
    '''This data object type describes uplink port ordering policy for a distributed
    virtual port. A uplink port can be in the active list, the standby list, or
    neither. It cannot be in both lists.'''
    
    obj = vim.client.factory.create('ns0:VMwareUplinkPortOrderPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'inherited', 'activeUplinkPort', 'standbyUplinkPort' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    