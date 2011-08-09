
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComputeResourceSummary(DynamicData):
    '''This data object type encapsulates a typical set of ComputeResource information
        that is useful for list views and summary pages.
    '''
    
    def __init__(self, effectiveCpu, effectiveMemory, numCpuCores, numCpuThreads, numEffectiveHosts, numHosts, overallStatus, totalCpu, totalMemory):
        # MUST define these
        super(ComputeResourceSummary, self).__init__()
    
        self.data['effectiveCpu'] = effectiveCpu
        self.data['effectiveMemory'] = effectiveMemory
        self.data['numCpuCores'] = numCpuCores
        self.data['numCpuThreads'] = numCpuThreads
        self.data['numEffectiveHosts'] = numEffectiveHosts
        self.data['numHosts'] = numHosts
        self.data['overallStatus'] = overallStatus
        self.data['totalCpu'] = totalCpu
        self.data['totalMemory'] = totalMemory
    
    
    @property
    def effectiveCpu(self):
        '''Effective CPU resources (in MHz) available to run virtual machines. This is the
        aggregated effective resource level from all running hosts. Hosts that are
        in maintenance mode or are unresponsive are not counted. Resources used by
        the VMware Service Console are not included in the aggregate. This value
        represents the amount of resources available for the root resource pool
        for running virtual machines.
        '''
        return self.data['effectiveCpu']

    @property
    def effectiveMemory(self):
        '''Effective memory resources (in MB) available to run virtual machines. This is the
        aggregated effective resource level from all running hosts. Hosts that are
        in maintenance mode or are unresponsive are not counted. Resources used by
        the VMware Service Console are not included in the aggregate. This value
        represents the amount of resources available for the root resource pool
        for running virtual machines.
        '''
        return self.data['effectiveMemory']

    @property
    def numCpuCores(self):
        '''Number of physical CPU cores. Physical CPU cores are the processors contained by a
        CPU package.
        '''
        return self.data['numCpuCores']

    @property
    def numCpuThreads(self):
        '''Aggregated number of CPU threads.
        '''
        return self.data['numCpuThreads']

    @property
    def numEffectiveHosts(self):
        '''Total number of effective hosts.
        '''
        return self.data['numEffectiveHosts']

    @property
    def numHosts(self):
        '''Total number of hosts.
        '''
        return self.data['numHosts']

    @property
    def overallStatus(self):
        '''Overall alarm status.
        '''
        return self.data['overallStatus']

    @property
    def totalCpu(self):
        '''Aggregated CPU resources of all hosts, in MHz.
        '''
        return self.data['totalCpu']

    @property
    def totalMemory(self):
        '''Aggregated memory resources of all hosts, in bytes.
        '''
        return self.data['totalMemory']

