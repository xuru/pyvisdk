
from pyvisdk.do.cluster_das_admission_control_info import ClusterDasAdmissionControlInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterFailoverResourcesAdmissionControlInfo(ClusterDasAdmissionControlInfo):
    '''The current admission control related information if the cluster was configured
        with a FailoverResourcesAdmissionControlPolicy.
    '''
    
    def __init__(self, currentCpuFailoverResourcesPercent, currentMemoryFailoverResourcesPercent):
        # MUST define these
        super(ClusterFailoverResourcesAdmissionControlInfo, self).__init__()
    
        self.data['currentCpuFailoverResourcesPercent'] = currentCpuFailoverResourcesPercent
        self.data['currentMemoryFailoverResourcesPercent'] = currentMemoryFailoverResourcesPercent
    
    
    @property
    def currentCpuFailoverResourcesPercent(self):
        '''The percentage of cpu resources in the cluster available for failover.
        '''
        return self.data['currentCpuFailoverResourcesPercent']

    @property
    def currentMemoryFailoverResourcesPercent(self):
        '''The percentage of memory resources in the cluster available for failover.
        '''
        return self.data['currentMemoryFailoverResourcesPercent']

