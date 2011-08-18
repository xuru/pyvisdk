# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineVMCIDeviceOption(vim, *args, **kwargs):
    '''The VirtualMachineVMCIDeviceOption data object contains the options for the
    virtual VMCI device (VirtualMachineVMCIDevice).'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineVMCIDeviceOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type', 'allowUnrestrictedCommunication' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    