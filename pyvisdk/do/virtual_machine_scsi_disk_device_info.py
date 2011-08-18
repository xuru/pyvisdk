# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

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
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'configurationTag', 'name', 'capacity', 'vm', 'disk', 'lunNumber',
        'transportHint' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    