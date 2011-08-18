# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmDasUpdateErrorEvent(vim, *args, **kwargs):
    '''The event records that an error occured when updating the HA agents with the
    current state of the virtual machine. If this occurs during a powerOn
    operation, the virtual machine will not be failed over in the event of a host
    failure. If it occurs during a powerOff, the virtual machine will be
    automatically powered on if the host it was last running on crashes.'''
    
    obj = vim.client.factory.create('ns0:VmDasUpdateErrorEvent')
    
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
    