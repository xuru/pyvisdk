# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualVmxnet3(vim, *args, **kwargs):
    '''The VirtualVmxnet3 data object type represents an instance of the Vmxnet3
    virtual Ethernet adapter attached to a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualVmxnet3')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'key', 'unitNumber',
        'addressType' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    