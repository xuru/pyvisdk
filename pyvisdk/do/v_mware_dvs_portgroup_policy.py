# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareDVSPortgroupPolicy(vim, *args, **kwargs):
    '''This class defines the VMware specific configuration for
    DistributedVirtualPort.'''
    
    obj = vim.client.factory.create('ns0:VMwareDVSPortgroupPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 8:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'blockOverrideAllowed', 'livePortMovingAllowed', 'portConfigResetAtDisconnect',
        'shapingOverrideAllowed', 'vendorConfigOverrideAllowed',
        'securityPolicyOverrideAllowed', 'uplinkTeamingOverrideAllowed',
        'vlanOverrideAllowed' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    