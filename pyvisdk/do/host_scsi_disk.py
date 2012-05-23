
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostScsiDisk(vim, *args, **kwargs):
    '''This data object type describes a SCSI disk. A SCSI disk contains a partition
    table which can be changed. To change a SCSI disk, use the device name and the
    partition specification.See RetrieveDiskPartitionInfoSee UpdateDiskPartitions'''
    
    obj = vim.client.factory.create('ns0:HostScsiDisk')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'capacity', 'devicePath', 'lunType', 'operationalState', 'uuid', 'deviceName',
        'deviceType' ]
    optional = [ 'ssd', 'alternateName', 'canonicalName', 'capabilities', 'descriptor',
        'displayName', 'durableName', 'key', 'model', 'queueDepth', 'revision',
        'scsiLevel', 'serialNumber', 'standardInquiry', 'vendor', 'vStorageSupport',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    