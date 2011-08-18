# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSFailureCriteria(vim, *args, **kwargs):
    '''This data object type describes the network adapter failover detection
    algorithm for a network adapter team.'''
    
    obj = vim.client.factory.create('ns0:DVSFailureCriteria')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'inherited', 'checkBeacon', 'checkDuplex', 'checkErrorPercent', 'checkSpeed',
        'fullDuplex', 'percentage', 'speed' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    