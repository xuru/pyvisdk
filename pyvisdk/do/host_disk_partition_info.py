# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionInfo(vim, *args, **kwargs):
    '''Information about the partitions on a disk. A DiskPartitionInfo object provides
    two different views into the partitions on a disk:See RetrieveDiskPartitionInfo
    See ComputeDiskPartitionInfo See UpdateDiskPartitions'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'deviceName', 'layout', 'spec' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    