# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostScsiDisk(vim, *args, **kwargs):
    '''This data object type describes a SCSI disk. A SCSI disk contains a partition
    table which can be changed. To change a SCSI disk, use the device name and the
    partition specification. See RetrieveDiskPartitionInfo See UpdateDiskPartitions'''
    
    obj = vim.client.factory.create('ns0:HostScsiDisk')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'deviceType', 'alternateName', 'canonicalName', 'capabilities',
        'descriptor', 'displayName', 'durableName', 'key', 'lunType', 'model',
        'operationalState', 'queueDepth', 'revision', 'scsiLevel', 'serialNumber',
        'standardInquiry', 'uuid', 'vendor', 'vStorageSupport', 'capacity',
        'devicePath' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    