# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmNoCompatibleHostForSecondaryEvent(vim, *args, **kwargs):
    '''This event records that no compatible host was found to place a secondary VM. A
    default alarm will be triggered upon this event, which by default would trigger
    a SNMP trap.'''
    
    obj = vim.client.factory.create('ns0:VmNoCompatibleHostForSecondaryEvent')
    
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
    