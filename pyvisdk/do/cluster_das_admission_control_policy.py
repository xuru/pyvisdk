# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasAdmissionControlPolicy(vim, *args, **kwargs):
    '''Base class for specifying how admission control should be done for VMware HA.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasAdmissionControlPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [  ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    