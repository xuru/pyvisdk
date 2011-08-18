# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineScsiDiskDeviceInfo(vim, *args, **kwargs):
    '''The ScsiDiskDeviceInfo class contains detailed information about a specific
    scsi disk hardware device. These devices are for the
    vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineScsiDiskDeviceInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'configurationTag', 'name', 'capacity', 'vm', 'disk', 'lunNumber',
        'transportHint' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    