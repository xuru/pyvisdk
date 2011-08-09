
from pyvisdk.do.scsi_lun import ScsiLun
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostScsiDisk(ScsiLun):
    '''This data object type describes a SCSI disk. A SCSI disk contains a partition
        table which can be changed. To change a SCSI disk, use the device name and
        the partition specification. See RetrieveDiskPartitionInfo See
        UpdateDiskPartitions
    '''
    
    def __init__(self, capacity, devicePath):
        # MUST define these
        super(HostScsiDisk, self).__init__()
    
        self.data['capacity'] = capacity
        self.data['devicePath'] = devicePath
    
    
    @property
    def capacity(self):
        '''The size of SCSI disk using the Logical Block Addressing scheme.
        '''
        return self.data['capacity']

    @property
    def devicePath(self):
        '''The device path of the ScsiDisk. This device path is a file path that can be
        opened to create partitions on the disk.
        '''
        return self.data['devicePath']

