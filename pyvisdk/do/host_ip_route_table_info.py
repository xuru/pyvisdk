# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostIpRouteTableInfo(vim, *args, **kwargs):
    '''IpRouteTableInfo. This is the list of all static routes on the host'''
    
    obj = vim.client.factory.create('ns0:HostIpRouteTableInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'ipRoute', 'ipv6Route' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    