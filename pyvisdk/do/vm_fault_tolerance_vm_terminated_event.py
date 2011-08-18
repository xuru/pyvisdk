# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmFaultToleranceVmTerminatedEvent(vim, *args, **kwargs):
    '''This event records a secondary or primary VM is terminated. The reason could be
    : divergence, lost connection to secondary, partial hardware failure of
    secondary, or by user.'''
    
    obj = vim.client.factory.create('ns0:VmFaultToleranceVmTerminatedEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'template', 'reason' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    