# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSNameArrayUplinkPortPolicy(vim, *args, **kwargs):
    '''The uplink port policy specifies an array of uniform names for the uplink ports
    across the hosts. The size of the array indicates the number of uplink ports
    that will be created for each host in the switch.When the names in this array
    change, the uplink ports on all the hosts are automatically renamed
    accordingly. Increasing the number of names in the array automatically creates
    additional uplink ports bearing the added name on each host. Decreasing the
    number of name automatically deletes the unused uplink ports on each host.
    Decreasing beyond the number of unused uplink port raises a fault.This policy
    overrides the portgroup's port naming format, if both are defined and the
    uplink ports are created in a uplink portgroup.'''
    
    obj = vim.client.factory.create('ns0:DVSNameArrayUplinkPortPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'uplinkPortName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    