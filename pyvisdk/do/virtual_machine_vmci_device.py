# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineVMCIDevice(vim, *args, **kwargs):
    '''The VirtualMachineVMCIDevice data object represents a virtual communication
    device that supports the VMCI (Virtual Machine Communication Interface). Each
    virtual machine has a VMCI device that handles interprocess socket-based
    communication. VMCI device information is available in the virtual machine
    hardware device list (VirtualMachine.config.hardware.device[]).An application
    running on a virtual machine uses the VMCI Sockets API for communication with
    other virtual machines on the same host, or for communication with the host.
    For information about using the vSphere VMCI Sockets API, see the .'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineVMCIDevice')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'key', 'unitNumber',
        'allowUnrestrictedCommunication', 'id' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    