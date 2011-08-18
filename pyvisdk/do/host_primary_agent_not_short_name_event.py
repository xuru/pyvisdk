# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPrimaryAgentNotShortNameEvent(vim, *args, **kwargs):
    '''This event records that the primary agent specified is not a short name. The
    name of the primary agent is usually stored as a short name. You should not
    normally see this error. Please check the network configurations of your hosts.'''
    
    obj = vim.client.factory.create('ns0:HostPrimaryAgentNotShortNameEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'primaryAgent' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    