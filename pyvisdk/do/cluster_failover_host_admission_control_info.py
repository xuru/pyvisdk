
from pyvisdk.do.cluster_das_admission_control_info import ClusterDasAdmissionControlInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterFailoverHostAdmissionControlInfo(ClusterDasAdmissionControlInfo):
    '''The current admission control related information if the cluster was configured
        with a FailoverHostAdmissionControlPolicy.
    '''
    
    def __init__(self, hostStatus):
        # MUST define these
        super(ClusterFailoverHostAdmissionControlInfo, self).__init__()
    
        self.data['hostStatus'] = hostStatus
    
    
    @property
    def hostStatus(self):
        '''Status of the failover hosts in the cluster.
        '''
        return self.data['hostStatus']

