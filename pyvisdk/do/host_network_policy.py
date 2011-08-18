# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkPolicy(vim, *args, **kwargs):
    '''This data object type describes network policies that can be configured for
    both virtual switches and port groups. The policy settings on the port group
    can inherit policy settings from their containing virtual switch. These policy
    settings are inherited if the settings on the port group are not set. Since
    every policy setting on a port group is optional, every individual policy
    setting can be inherited.By contrast, if a host is capable of implementing a
    policy setting, every virtual switch has some value assigned to the policy
    setting. In this case, although all of the policy settings are optional, they
    always have some value either by inheritance or by direct setting.Policy
    settings are organized into policy groups such as SecurityPolicy. Policy groups
    are optional since it is possible that a host may not implement such policies.
    If a host does not support a policy group, the policy group is not set on both
    the virtual switches and the port groups. See HostNetCapabilities'''
    
    obj = vim.client.factory.create('ns0:HostNetworkPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'nicTeaming', 'offloadPolicy', 'security', 'shapingPolicy' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    