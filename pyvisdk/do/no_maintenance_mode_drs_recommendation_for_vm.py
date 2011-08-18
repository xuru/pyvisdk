# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NoMaintenanceModeDrsRecommendationForVM(vim, *args, **kwargs):
    '''This event records that DRS did not recommend a migration for a powered on
    virtual machine, even though its host is going into maintenance mode. DRS may
    not be able to recommend a migration for a virtual machine for reasons, include
    but not limited to:* No other connected host is compatible with this virtual
    machine. * None of the other compatible hosts have sufficient resources to
    satisfy the reservation requirements of this virtual machine. * Moving to any
    other host would violate a DRS rule. For example, all other compatible hosts
    have some incompatible virtual machines running. * DRS is disabled on this
    virtual machine. * This virtual machine was still in the process of migrating
    into the host going into maintenance mode and was not considered by DRS. * This
    virtual machine was in the process of migrating to another host when the host
    tried to enter maintenance mode.'''
    
    obj = vim.client.factory.create('ns0:NoMaintenanceModeDrsRecommendationForVM')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'template' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    