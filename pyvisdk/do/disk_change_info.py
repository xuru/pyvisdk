
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DiskChangeInfo(DynamicData):
    '''Data structure to describe areas in a disk associated with this VM that have been
        modified since a well-defined point in the past. Returned by
        QueryChangedDiskAreas. This data structure describes a subset of the disk
        identified by startOffset and length. All areas that have been modified
        within this interval are listed under changedArea.
    '''
    
    def __init__(self, changedArea, length, startOffset):
        # MUST define these
        super(DiskChangeInfo, self).__init__()
    
        self.data['changedArea'] = changedArea
        self.data['length'] = length
        self.data['startOffset'] = startOffset
    
    
    @property
    def changedArea(self):
        '''Modified disk areas. Might be empty if no parts of the disk between startOffset
        and startOffset + length were modified.
        '''
        return self.data['changedArea']

    @property
    def length(self):
        '''Length (in bytes) of disk area described by this data structure.
        '''
        return self.data['length']

    @property
    def startOffset(self):
        '''Start offset (in bytes) of disk area described by this data structure.
        '''
        return self.data['startOffset']

