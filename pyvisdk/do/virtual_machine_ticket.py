# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineTicket(vim, *args, **kwargs):
    '''This data object contains the information needed to establish a connection to a
    running virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineTicket')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cfgFile', 'host', 'port', 'sslThumbprint', 'ticket' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    