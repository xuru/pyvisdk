# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVPortgroupPolicy(vim, *args, **kwargs):
    '''The DistributedVirtualPortgroup policies. This field is not applicable when
    queried directly against an ESX host.'''
    
    obj = vim.client.factory.create('ns0:DVPortgroupPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'blockOverrideAllowed', 'livePortMovingAllowed', 'portConfigResetAtDisconnect',
        'shapingOverrideAllowed', 'vendorConfigOverrideAllowed' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    