# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchPortStatistics(vim, *args, **kwargs):
    '''Statistic data of a DistributedVirtualPort.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchPortStatistics')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 16:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bytesInBroadcast', 'bytesInMulticast', 'bytesInUnicast', 'bytesOutBroadcast',
        'bytesOutMulticast', 'bytesOutUnicast', 'packetsInBroadcast',
        'packetsInDropped', 'packetsInException', 'packetsInMulticast',
        'packetsInUnicast', 'packetsOutBroadcast', 'packetsOutDropped',
        'packetsOutException', 'packetsOutMulticast', 'packetsOutUnicast' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    