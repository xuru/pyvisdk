# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchPortConnection(vim, *args, **kwargs):
    '''The class that represents a connection or an association between
    DistributedVirtualPort and a vNIC or pNIC.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchPortConnection')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'connectionCookie', 'portgroupKey', 'portKey', 'switchUuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    