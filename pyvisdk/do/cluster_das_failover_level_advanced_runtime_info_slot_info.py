# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo(vim, *args, **kwargs):
    '''A slot represents an amount of resources sufficient for any powered on virtual
    machine in the cluster.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cpuMHz', 'memoryMB', 'numVcpus' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    