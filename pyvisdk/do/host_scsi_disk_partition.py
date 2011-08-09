
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostScsiDiskPartition(DynamicData):
    '''This data object type describes the specification of a Disk partition.
    '''
    
    def __init__(self, diskName, partition):
        # MUST define these
        super(HostScsiDiskPartition, self).__init__()
    
        self.data['diskName'] = diskName
        self.data['partition'] = partition
    
    
    @property
    def diskName(self):
        '''The SCSI disk device on which a VMware File System (VMFS) extent resides.
        '''
        return self.data['diskName']

    @property
    def partition(self):
        '''The partition number of the partition on the ScsiDisk.
        '''
        return self.data['partition']

