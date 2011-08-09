
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCpuInfo(DynamicData):
    '''Information about the CPUs.
    '''
    
    def __init__(self, hz, numCpuCores, numCpuPackages, numCpuThreads):
        # MUST define these
        super(HostCpuInfo, self).__init__()
    
        self.data['hz'] = hz
        self.data['numCpuCores'] = numCpuCores
        self.data['numCpuPackages'] = numCpuPackages
        self.data['numCpuThreads'] = numCpuThreads
    
    
    @property
    def hz(self):
        '''CPU speed per core. This might be an averaged value if the speed is not uniform
        across all cores. The total CPU speed of the box is defined as hz *
        numCpuCores
        '''
        return self.data['hz']

    @property
    def numCpuCores(self):
        '''Number of physical CPU cores on the host.
        '''
        return self.data['numCpuCores']

    @property
    def numCpuPackages(self):
        '''Number of physical CPU packages on the host.
        '''
        return self.data['numCpuPackages']

    @property
    def numCpuThreads(self):
        '''Number of physical CPU threads on the host.
        '''
        return self.data['numCpuThreads']

