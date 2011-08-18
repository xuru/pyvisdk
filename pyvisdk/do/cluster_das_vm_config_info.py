# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasVmConfigInfo(vim, *args, **kwargs):
    '''The ClusterDasVmConfigInfo data object contains the HA configuration for a
    single virtual machine.All fields are optional. If you set the parameter to
    when you call ReconfigureComputeResource_Task, an unset property has no effect
    on the existing property value in the cluster configuration on the Server. If
    you set the parameter to when you reconfigure a cluster, the cluster
    configuration is reverted to the default values, then the new configuration
    values are applied.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasVmConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dasSettings', 'key', 'powerOffOnIsolation', 'restartPriority' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    