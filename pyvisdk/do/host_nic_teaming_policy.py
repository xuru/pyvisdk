# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNicTeamingPolicy(vim, *args, **kwargs):
    '''Policy for a network adapter team.'''
    
    obj = vim.client.factory.create('ns0:HostNicTeamingPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'failureCriteria', 'nicOrder', 'notifySwitches', 'policy', 'reversePolicy',
        'rollingOrder' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    