# -*- coding: ascii -*-

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
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'cpuFeatureMask', 'family', 'fullName', 'id', 'recommendedColorDepth',
        'recommendedDiskController', 'recommendedDiskSizeMB',
        'recommendedEthernetCard', 'recommendedMemMB', 'recommendedSCSIController',
        'supportedDiskControllerList', 'supportedEthernetCard', 'supportedMaxCPUs',
        'supportedMaxMemMB', 'supportedMinMemMB', 'supportedNumDisks',
        'supportsCpuHotAdd', 'supportsCpuHotRemove', 'supportsMemoryHotAdd',
        'supportsSlaveDisk', 'supportsVMI', 'supportsWakeOnLan' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    