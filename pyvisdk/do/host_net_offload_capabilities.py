# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetOffloadCapabilities(vim, *args, **kwargs):
    '''Offload capabilities are used to optimize virtual machine network performance.
    When a virtual machine is transmitting on a network, some operations can be
    offloaded either to the host or to physical hardware. This data object type
    defines the set of offload capabilities that may be available on a host.This
    data object type is used both to publish the list of offload capabilities and
    to contain offload capability policy settings. The network policy logic is
    built on a two-level inheritance scheme which requires that all settings be
    optional. As a result, all properties on the NetOffloadCapabilities object must
    be optional. See HostNetworkPolicy'''
    
    obj = vim.client.factory.create('ns0:HostNetOffloadCapabilities')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'csumOffload', 'tcpSegmentation', 'zeroCopyXmit' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    