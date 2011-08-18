# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterAntiAffinityRuleSpec(vim, *args, **kwargs):
    '''The ClusterAntiAffinityRuleSpec data object defines a set of virtual machines.
    DRS will attempt to schedule the virtual machines to run on different hosts.'''
    
    obj = vim.client.factory.create('ns0:ClusterAntiAffinityRuleSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'inCompliance', 'key', 'mandatory', 'name', 'status', 'userCreated',
        'vm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    