
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskDimensionsChs(DynamicData):
    '''This data object type describes dimensions using the cylinder, head, sector (CHS)
        coordinate system. This coordinate system is generally needed for
        partitioning for legacy reasons. When defining partitions, many
        partitioning utilities do not function correctly when certain CHS
        constraints are not met.
    '''
    
    def __init__(self, cylinder, head, sector):
        # MUST define these
        super(HostDiskDimensionsChs, self).__init__()
    
        self.data['cylinder'] = cylinder
        self.data['head'] = head
        self.data['sector'] = sector
    
    
    @property
    def cylinder(self):
        '''The number of cylinders.
        '''
        return self.data['cylinder']

    @property
    def head(self):
        '''The number of heads per cylinders.
        '''
        return self.data['head']

    @property
    def sector(self):
        '''The number of sectors per head.
        '''
        return self.data['sector']

