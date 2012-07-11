
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def GuestOsDescriptor(vim, *args, **kwargs):
    '''This data object type contains information to describe a particular guest
    operating system.'''
    
    obj = vim.client.factory.create('ns0:GuestOsDescriptor')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 30:
        raise IndexError('Expected at least 31 arguments got: %d' % len(args))

    required = [ 'family', 'fullName', 'ich7mRecommended', 'id', 'numSupportedCoresPerSocket',
        'numSupportedPhysicalSockets', 'recommendedColorDepth',
        'recommendedDiskController', 'recommendedDiskSizeMB', 'recommendedFirmware',
        'recommendedMemMB', 'smcRecommended', 'smcRequired',
        'supportedDiskControllerList', 'supportedEthernetCard', 'supportedFirmware',
        'supportedForCreate', 'supportedMaxCPUs', 'supportedMaxMemMB',
        'supportedMinMemMB', 'supportedNumDisks', 'supportLevel', 'supports3D',
        'supportsCpuHotAdd', 'supportsCpuHotRemove', 'supportsMemoryHotAdd',
        'supportsVMI', 'supportsWakeOnLan', 'usbRecommended', 'vRAMSizeInKB' ]
    optional = [ 'cpuFeatureMask', 'recommendedEthernetCard', 'recommendedSCSIController',
        'recommendedUSBController', 'supportedUSBControllerList', 'supportsSlaveDisk',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    