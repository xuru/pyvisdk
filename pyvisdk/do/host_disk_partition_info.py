
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskPartitionInfo(DynamicData):
    '''Information about the partitions on a disk. A DiskPartitionInfo object provides
        two different views into the partitions on a disk:* A detailed
        specification that is used to create the partition table. * A convenient
        view that shows the allocations of blocks as a contiguous sequence of
        block ranges.See RetrieveDiskPartitionInfo See ComputeDiskPartitionInfo
        See UpdateDiskPartitions
    '''
    
    def __init__(self, deviceName, layout, spec):
        # MUST define these
        super(HostDiskPartitionInfo, self).__init__()
    
        self.data['deviceName'] = deviceName
        self.data['layout'] = layout
        self.data['spec'] = spec
    
    
    @property
    def deviceName(self):
        '''The device name of the disk to which this partition information corresponds.
        '''
        return self.data['deviceName']

    @property
    def layout(self):
        '''A convenient format for describing disk layout. This layout specification can be
        converted to a Specification object.
        '''
        return self.data['layout']

    @property
    def spec(self):
        '''The detailed disk partition specification. Use this specification for manipulating
        the file system.
        '''
        return self.data['spec']

