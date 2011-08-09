
from pyvisdk.do.virtual_disk_raw_disk_ver2_backing_info import VirtualDiskRawDiskVer2BackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskPartitionedRawDiskVer2BackingInfo(VirtualDiskRawDiskVer2BackingInfo):
    '''This data object type contains information about backing a virtual disk using one
        or more partitions on a physical disk device. This type of backing is
        supported for VMware Server.
    '''
    
    def __init__(self, partition):
        # MUST define these
        super(VirtualDiskPartitionedRawDiskVer2BackingInfo, self).__init__()
    
        self.data['partition'] = partition
    
    
    @property
    def partition(self):
        '''Array of partition indexes. This array identifies the partitions that are used on
        the physical disk drive.
        '''
        return self.data['partition']

