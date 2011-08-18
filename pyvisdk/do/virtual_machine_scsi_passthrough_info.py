# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineScsiPassthroughInfo(vim, *args, **kwargs):
    '''Description of a generic SCSI device, including information about the device
    ID.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineScsiPassthroughInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configurationTag', 'name', 'physicalUnitNumber', 'scsiClass', 'vendor' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    