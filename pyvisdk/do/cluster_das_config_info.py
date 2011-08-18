# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasConfigInfo(vim, *args, **kwargs):
    '''The ClusterDasConfigInfo data object contains configuration data about the HA
    service on a cluster.All fields are optional. If you set the parameter to when
    you call ReconfigureComputeResource_Task, an unset property has no effect on
    the existing property value in the cluster configuration on the Server. If you
    set the parameter to when you reconfigure a cluster, the cluster configuration
    is reverted to the default values, then the new configuration values are
    applied.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'admissionControlEnabled', 'admissionControlPolicy', 'defaultVmSettings',
        'enabled', 'failoverLevel', 'hostMonitoring', 'option', 'vmMonitoring' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    