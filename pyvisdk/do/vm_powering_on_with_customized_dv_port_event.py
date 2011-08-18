# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmPoweringOnWithCustomizedDVPortEvent(vim, *args, **kwargs):
    '''This event records when a virtual machine was powering on using DVPorts with
    port level configuration, which might be different from the DVportgroup.'''
    
    obj = vim.client.factory.create('ns0:VmPoweringOnWithCustomizedDVPortEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'template', 'vnic' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    