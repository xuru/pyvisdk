
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class InventoryDescription(DynamicData):
    '''Data object to capture all information needed to describe a sample inventory.
    '''
    
    def __init__(self, numClusters, numCpuDev, numDiskDev, numHosts, numNetDev, numResourcePools, numvCpuDev, numvDiskDev, numVirtualMachines, numvNetDev):
        # MUST define these
        super(InventoryDescription, self).__init__()
    
        self.data['numClusters'] = numClusters
        self.data['numCpuDev'] = numCpuDev
        self.data['numDiskDev'] = numDiskDev
        self.data['numHosts'] = numHosts
        self.data['numNetDev'] = numNetDev
        self.data['numResourcePools'] = numResourcePools
        self.data['numvCpuDev'] = numvCpuDev
        self.data['numvDiskDev'] = numvDiskDev
        self.data['numVirtualMachines'] = numVirtualMachines
        self.data['numvNetDev'] = numvNetDev
    
    
    @property
    def numClusters(self):
        '''The number of clusters. Default value is equal to numHosts/5.
        '''
        return self.data['numClusters']

    @property
    def numCpuDev(self):
        '''The number cpu devices per host. Default value is 4.
        '''
        return self.data['numCpuDev']

    @property
    def numDiskDev(self):
        '''The number disk devices per host. Default value is 10.
        '''
        return self.data['numDiskDev']

    @property
    def numHosts(self):
        '''The number of hosts.
        '''
        return self.data['numHosts']

    @property
    def numNetDev(self):
        '''The number network devices per host. Default value is 2.
        '''
        return self.data['numNetDev']

    @property
    def numResourcePools(self):
        '''The number of resource pools. Default value is equal to numHosts
        '''
        return self.data['numResourcePools']

    @property
    def numvCpuDev(self):
        '''The number cpu devices per vm. Default value is 2.
        '''
        return self.data['numvCpuDev']

    @property
    def numvDiskDev(self):
        '''The number disk devices per vm. Default value is 4.
        '''
        return self.data['numvDiskDev']

    @property
    def numVirtualMachines(self):
        '''The number of virtual machines.
        '''
        return self.data['numVirtualMachines']

    @property
    def numvNetDev(self):
        '''The number network devices per vm. Default value is 1.
        '''
        return self.data['numvNetDev']

