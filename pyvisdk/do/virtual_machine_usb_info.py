# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineUsbInfo(vim, *args, **kwargs):
    '''This data object contains information about a physical USB device on the host.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineUsbInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configurationTag', 'name', 'description', 'family', 'physicalPath', 'product',
        'speed', 'summary', 'vendor' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    