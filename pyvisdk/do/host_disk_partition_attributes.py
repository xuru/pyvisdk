
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskPartitionAttributes(DynamicData):
    '''Information about a single disk partition. A partition is a contiguous set of
        blocks on a disk that is marked for use. The typeId identifies the purpose
        of the data in the partition.
    '''
    
    def __init__(self, attributes, endSector, logical, partition, startSector, type):
        # MUST define these
        super(HostDiskPartitionAttributes, self).__init__()
    
        self.data['attributes'] = attributes
        self.data['endSector'] = endSector
        self.data['logical'] = logical
        self.data['partition'] = partition
        self.data['startSector'] = startSector
        self.data['type'] = type
    
    
    @property
    def attributes(self):
        '''The attributes on the partition.
        '''
        return self.data['attributes']

    @property
    def endSector(self):
        '''The end sector.
        '''
        return self.data['endSector']

    @property
    def logical(self):
        '''The flag to indicate whether or not the partition is logical. If true, the
        partition number should be greater than 4.
        '''
        return self.data['logical']

    @property
    def partition(self):
        '''The partition number. Must be a positive integer.
        '''
        return self.data['partition']

    @property
    def startSector(self):
        '''The start sector.
        '''
        return self.data['startSector']

    @property
    def type(self):
        '''Type of data in the partition. If it is a well-known partition type, it will be
        one of the defined types. If it is not, then it will be reported as a
        hexadecimal number. For example, "none", "vmfs", "linux", and "0x20" are
        all valid values.
        '''
        return self.data['type']

