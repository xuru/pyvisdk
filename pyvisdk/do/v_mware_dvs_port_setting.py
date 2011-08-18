# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareDVSPortSetting(vim, *args, **kwargs):
    '''This class defines the VMware specific configuration for
    DistributedVirtualPort.'''
    
    obj = vim.client.factory.create('ns0:VMwareDVSPortSetting')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'blocked', 'inShapingPolicy', 'outShapingPolicy', 'vendorSpecificConfig',
        'vmDirectPathGen2Allowed', 'qosTag', 'securityPolicy', 'txUplink',
        'uplinkTeamingPolicy', 'vlan' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    