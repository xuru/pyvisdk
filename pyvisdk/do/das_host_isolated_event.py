# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DasHostIsolatedEvent(vim, *args, **kwargs):
    '''This event records that a host has been isolated from the network in a HA
    cluster. Since an isolated host cannot be distinguished from a failed host
    except by the isolated host itself, this event is logged when the isolated host
    regains network connectivity.'''
    
    obj = vim.client.factory.create('ns0:DasHostIsolatedEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'isolatedHost' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    