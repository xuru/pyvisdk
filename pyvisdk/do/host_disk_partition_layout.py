
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskPartitionLayout(DynamicData):
    '''This data object type describes the disk partition layout specified as a list of
        ordered BlockRanges. This view of the disk partitions shows the data on
        the disk as a contiguous set of BlockRanges.
    '''
    
    def __init__(self, partition, total):
        # MUST define these
        super(HostDiskPartitionLayout, self).__init__()
    
        self.data['partition'] = partition
        self.data['total'] = total
    
    
    @property
    def partition(self):
        '''List of block ranges on the disk.
        '''
        return self.data['partition']

    @property
    def total(self):
        '''Total number of blocks on a disk.
        '''
        return self.data['total']

