# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostCpuPowerManagementInfo(vim, *args, **kwargs):
    '''The CpuPowerManagementInfo data object type describes supported power
    management and current policy.'''
    
    obj = vim.client.factory.create('ns0:HostCpuPowerManagementInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'currentPolicy', 'hardwareSupport' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    