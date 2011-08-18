# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineLegacyNetworkSwitchInfo(vim, *args, **kwargs):
    '''The LegacyNetworkSwitchInfo data object type contains information about the
    legacy network switches available on the host.* VMware Server - Options
    available for the "custom" NetworkBackingType. * ESX Server - The "esxnet"
    NetworkBackingType.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineLegacyNetworkSwitchInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    