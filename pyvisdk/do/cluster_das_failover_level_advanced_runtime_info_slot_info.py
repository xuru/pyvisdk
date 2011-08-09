
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo(DynamicData):
    '''A slot represents an amount of resources sufficient for any powered on virtual
        machine in the cluster.
    '''
    
    def __init__(self, cpuMHz, memoryMB, numVcpus):
        # MUST define these
        super(ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo, self).__init__()
    
        self.data['cpuMHz'] = cpuMHz
        self.data['memoryMB'] = memoryMB
        self.data['numVcpus'] = numVcpus
    
    
    @property
    def cpuMHz(self):
        '''The cpu speed of a slot is defined as the maximum cpu reservation of any powered
        on virtual machine in the cluster, or any otherwise defined minimum,
        whichever is larger.
        '''
        return self.data['cpuMHz']

    @property
    def memoryMB(self):
        '''The memory size of a slot is defined as the maximum memory reservation plus memory
        overhead of any powered on virtual machine in the cluster, or any
        otherwise defined minimum, whichever is larger.
        '''
        return self.data['memoryMB']

    @property
    def numVcpus(self):
        '''The number of virtual cpus of a slot is defined as the maximum number of virtual
        cpus any powered on virtual machine has.
        '''
        return self.data['numVcpus']

