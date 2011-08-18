# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostSystemResourceInfo(vim, *args, **kwargs):
    '''The SystemResourceInfo data object describes the configuration of a single
    system resource group. System resource groups are analogous to ResourcePool
    objects for virtual machines; however, their structure is fixed and groups may
    not be created nor destroyed, only configured.'''
    
    obj = vim.client.factory.create('ns0:HostSystemResourceInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'child', 'config', 'key' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    