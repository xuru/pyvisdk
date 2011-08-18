# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskPartitionedRawDiskVer2BackingInfo(vim, *args, **kwargs):
    '''This data object type contains information about backing a virtual disk using
    one or more partitions on a physical disk device. This type of backing is
    supported for VMware Server.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskPartitionedRawDiskVer2BackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'deviceName', 'partition' ]
    inherited = [ 'useAutoDetect', 'changeId', 'descriptorFileName', 'uuid' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    