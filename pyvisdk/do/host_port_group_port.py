# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPortGroupPort(vim, *args, **kwargs):
    '''A Port data object type is a runtime representation of network connectivity
    between a network service or virtual machine and a virtual switch. This is
    different from a port group in that the port group represents the configuration
    aspects of the network connection. The Port object provides runtime statistics.'''
    
    obj = vim.client.factory.create('ns0:HostPortGroupPort')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'key', 'mac', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    