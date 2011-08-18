# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ConfigTarget(vim, *args, **kwargs):
    '''The ConfigTarget class contains information about "physical" devices that can
    be used to back virtual devices.'''
    
    obj = vim.client.factory.create('ns0:ConfigTarget')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'autoVmotion', 'cdRom', 'datastore', 'distributedVirtualPortgroup',
        'distributedVirtualSwitch', 'floppy', 'ideDisk', 'legacyNetworkInfo',
        'maxMemMBOptimalPerf', 'network', 'numCpuCores', 'numCpus', 'numNumaNodes',
        'parallel', 'pciPassthrough', 'resourcePool', 'scsiDisk', 'scsiPassthrough',
        'serial', 'sound', 'usb' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    