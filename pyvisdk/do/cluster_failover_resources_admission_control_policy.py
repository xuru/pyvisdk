
from pyvisdk.do.cluster_das_admission_control_policy import ClusterDasAdmissionControlPolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterFailoverResourcesAdmissionControlPolicy(ClusterDasAdmissionControlPolicy):
    '''The ClusterFailoverResourcesAdmissionControlPolicy reserves a specified percentage
        of aggregate cluster resources for failover. With the resources failover
        policy in place, VMware HA uses the following calculations to control
        virtual machine migration in the cluster.HA uses the actual reservations
        of the virtual machines. If a virtual machine does not have reservations,
        meaning that the reservation is 0, a default of 0MB memory and 256MHz CPU
        is applied. This is controlled by the same HA advanced options used for
        the failover level policy (ClusterFailoverLevelAdmissionControlPolicy).
    '''
    
    def __init__(self, cpuFailoverResourcesPercent, memoryFailoverResourcesPercent):
        # MUST define these
        super(ClusterFailoverResourcesAdmissionControlPolicy, self).__init__()
    
        self.data['cpuFailoverResourcesPercent'] = cpuFailoverResourcesPercent
        self.data['memoryFailoverResourcesPercent'] = memoryFailoverResourcesPercent
    
    
    @property
    def cpuFailoverResourcesPercent(self):
        '''Percentage of CPU resources in the cluster to reserve for failover. You can
        specify up to 100% of CPU resources for failover.
        '''
        return self.data['cpuFailoverResourcesPercent']

    @property
    def memoryFailoverResourcesPercent(self):
        '''Percentage of memory resources in the cluster to reserve for failover. You can
        specify up to 100% of memory resources for failover.
        '''
        return self.data['memoryFailoverResourcesPercent']

