# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterFailoverHostAdmissionControlInfoHostStatus(vim, *args, **kwargs):
    '''Data object containing the status of a failover host.'''
    
    obj = vim.client.factory.create('ns0:ClusterFailoverHostAdmissionControlInfoHostStatus')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'host', 'status' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    