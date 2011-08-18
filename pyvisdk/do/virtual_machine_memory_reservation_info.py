# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineMemoryReservationInfo(vim, *args, **kwargs):
    '''The VirtualMachineReservationInfo data object type describes the amount of
    memory that is being reserved for virtual machines on the host, and how
    additional memory may be acquired.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineMemoryReservationInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'allocationPolicy', 'virtualMachineMax', 'virtualMachineMin',
        'virtualMachineReserved' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    