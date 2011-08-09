
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskPartitionSpec(DynamicData):
    '''This data object type describes the disk partition table specification used to
        configure the partitions on a disk. This data object represents the
        fundamental data needed to specify a partition table.
    '''
    
    def __init__(self, chs, partition, totalSectors):
        # MUST define these
        super(HostDiskPartitionSpec, self).__init__()
    
        self.data['chs'] = chs
        self.data['partition'] = partition
        self.data['totalSectors'] = totalSectors
    
    
    @property
    def chs(self):
        '''Disk dimensions expressed as cylinder, head, sector (CHS) coordinates.
        '''
        return self.data['chs']

    @property
    def partition(self):
        '''List of partitions on the disk.
        '''
        return self.data['partition']

    @property
    def totalSectors(self):
        '''Disk dimensions expressed in total number of 512-byte sectors.
        '''
        return self.data['totalSectors']

