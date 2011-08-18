# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineMemoryReservationSpec(vim, *args, **kwargs):
    '''The VirtualMachineReservationSpec data object specifies configurable parameters
    for virtual machine memory reservation.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineMemoryReservationSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'allocationPolicy', 'virtualMachineReserved' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    