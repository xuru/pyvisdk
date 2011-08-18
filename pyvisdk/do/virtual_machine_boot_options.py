# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineBootOptions(vim, *args, **kwargs):
    '''The VirtualMachineBootOptions data object defines the boot-time behavior of a
    virtual machine.You can use the delay options to specify a time interval during
    which you can enter the virtual machine BIOS setup. These options provide a
    solution for the situation that occurs when the console attaches to the virtual
    machine after the boot sequence has passed the BIOS setup entry point.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineBootOptions')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bootDelay', 'bootRetryDelay', 'bootRetryEnabled', 'enterBIOSSetup' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    