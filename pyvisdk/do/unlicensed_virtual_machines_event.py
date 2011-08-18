# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def UnlicensedVirtualMachinesEvent(vim, *args, **kwargs):
    '''This event records that we have unlicensed virtual machines on the specified
    host. This can be both a (@link vim.ManagedEntity.configIssue configIssue) and
    an entry in the event log.'''
    
    obj = vim.client.factory.create('ns0:UnlicensedVirtualMachinesEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm',
        'available', 'unlicensed' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    