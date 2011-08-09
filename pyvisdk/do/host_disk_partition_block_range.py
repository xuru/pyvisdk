
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskPartitionBlockRange(DynamicData):
    '''A BlockRange data object type describes a contiguous set of blocks on a disk. A
        BlockRange may describe either a partition or unpartitioned (primordial)
        blocks on the disk.
    '''
    
    def __init__(self, end, partition, start, type):
        # MUST define these
        super(HostDiskPartitionBlockRange, self).__init__()
    
        self.data['end'] = end
        self.data['partition'] = partition
        self.data['start'] = start
        self.data['type'] = type
    
    
    @property
    def end(self):
        '''The end block address of the disk range. The block numbers start from zero. The
        range is inclusive of the end address.
        '''
        return self.data['end']

    @property
    def partition(self):
        '''Partition number. This number is a hint from the server indicating what the
        partition number for this block range is if the range corresponds to a
        partition. The partition number should correlate to the one in the
        partition specification. If sent back to the server, this property is
        ignored.
        '''
        return self.data['partition']

    @property
    def start(self):
        '''The starting block address of the disk range. The block numbers start from zero.
        The range is inclusive of the end address.
        '''
        return self.data['start']

    @property
    def type(self):
        '''The type of data in the partition.
        '''
        return self.data['type']

