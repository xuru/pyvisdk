# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasFailoverLevelAdvancedRuntimeInfo(vim, *args, **kwargs):
    '''Advanced runtime information related to the high availability service for a
    cluster that has been configured with a failover level admission control
    policy. See ClusterFailoverLevelAdmissionControlPolicy.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasFailoverLevelAdvancedRuntimeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dasHostInfo', 'hostSlots', 'slotInfo', 'totalGoodHosts', 'totalHosts',
        'totalSlots', 'totalVms', 'unreservedSlots', 'usedSlots' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    