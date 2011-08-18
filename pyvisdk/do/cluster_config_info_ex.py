# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterConfigInfoEx(vim, *args, **kwargs):
    '''The ClusterConfigInfoEx data object describes a complete cluster configuration.
    For information about configuring a cluster, see ClusterConfigSpecEx.'''
    
    obj = vim.client.factory.create('ns0:ClusterConfigInfoEx')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'vmSwapPlacement', 'dasConfig', 'dasVmConfig', 'dpmConfigInfo',
        'dpmHostConfig', 'drsConfig', 'drsVmConfig', 'group', 'rule' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    