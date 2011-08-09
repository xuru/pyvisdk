
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNumaInfo(DynamicData):
    '''Information about the NUMA (non-uniform memory access).
    '''
    
    def __init__(self, numaNode, numNodes, type):
        # MUST define these
        super(HostNumaInfo, self).__init__()
    
        self.data['numaNode'] = numaNode
        self.data['numNodes'] = numNodes
        self.data['type'] = type
    
    
    @property
    def numaNode(self):
        '''Information about each of the NUMA nodes on the host. The array is empty if the
        host is not NUMA-capable.
        '''
        return self.data['numaNode']

    @property
    def numNodes(self):
        '''The number of NUMA nodes on the host. The value is 0 if the host is not NUMA-
        capable.
        '''
        return self.data['numNodes']

    @property
    def type(self):
        '''The type of the NUMA. Currently there is only one value: "X440".
        '''
        return self.data['type']

