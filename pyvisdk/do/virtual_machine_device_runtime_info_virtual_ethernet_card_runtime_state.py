# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeState(vim, *args, **kwargs):
    '''Runtime state of a virtual ethernet card device.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeState')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'vmDirectPathGen2Active', 'vmDirectPathGen2InactiveReasonExtended',
        'vmDirectPathGen2InactiveReasonOther', 'vmDirectPathGen2InactiveReasonVm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    