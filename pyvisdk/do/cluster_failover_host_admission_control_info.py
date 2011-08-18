# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterFailoverHostAdmissionControlInfo(vim, *args, **kwargs):
    '''The current admission control related information if the cluster was configured
    with a FailoverHostAdmissionControlPolicy.'''
    
    obj = vim.client.factory.create('ns0:ClusterFailoverHostAdmissionControlInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'hostStatus' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    