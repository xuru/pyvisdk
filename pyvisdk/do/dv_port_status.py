# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVPortStatus(vim, *args, **kwargs):
    '''The runtime information of a DistributedVirtualPort.'''
    
    obj = vim.client.factory.create('ns0:DVPortStatus')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'blocked', 'linkPeer', 'linkUp', 'macAddress', 'mtu', 'statusDetail',
        'trunkingMode', 'vlanIds', 'vmDirectPathGen2Active',
        'vmDirectPathGen2InactiveReasonExtended',
        'vmDirectPathGen2InactiveReasonNetwork', 'vmDirectPathGen2InactiveReasonOther' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    