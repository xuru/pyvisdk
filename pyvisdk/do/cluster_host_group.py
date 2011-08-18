# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterHostGroup(vim, *args, **kwargs):
    '''The ClusterHostGroup data object identifies hosts for VM-Host rules. VM-Host
    rules determine placement of virtual machines on hosts in a cluster. The logic
    specified in a ClusterVmHostRuleInfo object determines where virtual machines
    can be powered-on.'''
    
    obj = vim.client.factory.create('ns0:ClusterHostGroup')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name', 'host' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    