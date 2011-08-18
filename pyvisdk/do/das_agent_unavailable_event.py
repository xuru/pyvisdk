# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DasAgentUnavailableEvent(vim, *args, **kwargs):
    '''This event records that VirtualCenter cannot contact any primary host in this
    HA cluster. HA designates some hosts as primary hosts in the HA cluster. When
    adding a new host to an existing cluster, HA needs to contact one of the
    primary hosts to finish the configuration. VirtualCenter has lost contact with
    all primary nodes in the connected state. Attempts to configure HA on a host in
    this cluster will fail until a DasAgentFoundEvent is logged or unless this is
    the first node to be configured. For example, if all the other hosts are
    disconnected first.'''
    
    obj = vim.client.factory.create('ns0:DasAgentUnavailableEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    