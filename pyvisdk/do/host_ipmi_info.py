# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostIpmiInfo(vim, *args, **kwargs):
    '''The IpmiInfo data object contains IPMI (Intelligent Platform Management
    Interface) and BMC (Baseboard Management Controller) information for the host.'''
    
    obj = vim.client.factory.create('ns0:HostIpmiInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bmcIpAddress', 'bmcMacAddress', 'login', 'password' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    