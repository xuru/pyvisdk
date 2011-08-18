# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNicIpHint(vim, *args, **kwargs):
    '''This data object type describes a network in network hint where the network is
    specified using IP addresses, for example, 10.27.49.1-10.27.49.254'''
    
    obj = vim.client.factory.create('ns0:PhysicalNicIpHint')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'vlanId', 'ipSubnet' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    