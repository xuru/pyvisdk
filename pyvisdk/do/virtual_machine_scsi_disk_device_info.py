
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
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'name' ]
    optional = [ 'disk', 'lunNumber', 'transportHint', 'capacity', 'vm', 'configurationTag',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    