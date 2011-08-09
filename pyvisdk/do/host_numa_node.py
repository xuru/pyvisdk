
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNumaNode(DynamicData):
    '''Information about a single NUMA node.NOTE: This data object is not modeled
        correctly if the NUMA node contains multiple disjoint memory ranges. If
        there are multiple memory ranges, the client will see one memory ranges
        from this NumaNode object, and the memory range may or may not belong to
        this NUMA node.
    '''
    
    def __init__(self, cpuID, memoryRangeBegin, memoryRangeLength, typeId):
        # MUST define these
        super(HostNumaNode, self).__init__()
    
        self.data['cpuID'] = cpuID
        self.data['memoryRangeBegin'] = memoryRangeBegin
        self.data['memoryRangeLength'] = memoryRangeLength
        self.data['typeId'] = typeId
    
    
    @property
    def cpuID(self):
        '''Information about each of the CPUs associated with the node.
        '''
        return self.data['cpuID']

    @property
    def memoryRangeBegin(self):
        '''Beginning memory range for this NUMA node.
        '''
        return self.data['memoryRangeBegin']

    @property
    def memoryRangeLength(self):
        '''Length of the memory range for this node in bytes, that is, the amount of memory
        on the node.
        '''
        return self.data['memoryRangeLength']

    @property
    def typeId(self):
        '''Zero-based NUMA ID for the node.
        '''
        return self.data['typeId']

