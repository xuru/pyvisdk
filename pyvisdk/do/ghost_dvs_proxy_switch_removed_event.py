# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def GhostDvsProxySwitchRemovedEvent(vim, *args, **kwargs):
    '''This event records when the ghost DVS proxy switches (a.k.a host proxy switches
    that don't match any DVS defined in Virtual Center) were removed on the host.'''
    
    obj = vim.client.factory.create('ns0:GhostDvsProxySwitchRemovedEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'switchUuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    