# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchHostMemberPnicSpec(vim, *args, **kwargs):
    '''Specification to select individual physical NICs. In this case, a proxy switch
    will be created on the host from scratch with the pNICs as the uplinks.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchHostMemberPnicSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'connectionCookie', 'pnicDevice', 'uplinkPortgroupKey', 'uplinkPortKey' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    