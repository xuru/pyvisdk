
from pyvisdk.do.cluster_das_admission_control_info import ClusterDasAdmissionControlInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterFailoverLevelAdmissionControlInfo(ClusterDasAdmissionControlInfo):
    '''The current admission control related information if the cluster was configured
        with a FailoverLevelAdmissionControlPolicy.
    '''
    
    def __init__(self, currentFailoverLevel):
        # MUST define these
        super(ClusterFailoverLevelAdmissionControlInfo, self).__init__()
    
        self.data['currentFailoverLevel'] = currentFailoverLevel
    
    
    @property
    def currentFailoverLevel(self):
        '''Current failover level. This is the number of physical host failures that can be
        tolerated without impacting the ability to satisfy the minimums for all
        running virtual machines. This represents the current value, as opposed to
        desired value configured by the user.
        '''
        return self.data['currentFailoverLevel']

