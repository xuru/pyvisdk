
from pyvisdk.do.compute_resource_summary import ComputeResourceSummary
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterComputeResourceSummary(ComputeResourceSummary):
    '''The ClusterComputeResourceSummary data object encapsulates runtime properties of a
        ClusterComputeResource.
    '''
    
    def __init__(self, admissionControlInfo, currentBalance, currentEVCModeKey, currentFailoverLevel, numVmotions, targetBalance):
        # MUST define these
        super(ClusterComputeResourceSummary, self).__init__()
    
        self.data['admissionControlInfo'] = admissionControlInfo
        self.data['currentBalance'] = currentBalance
        self.data['currentEVCModeKey'] = currentEVCModeKey
        self.data['currentFailoverLevel'] = currentFailoverLevel
        self.data['numVmotions'] = numVmotions
        self.data['targetBalance'] = targetBalance
    
    
    @property
    def admissionControlInfo(self):
        '''Information about the current amount of resources available for a VMware HA
        cluster. The actual type of admissionControlInfo will depend on what kind
        of ClusterDasAdmissionControlPolicy was used to configure the cluster.
        '''
        return self.data['admissionControlInfo']

    @property
    def currentBalance(self):
        '''The current balance, in terms of standard deviation, for a DRS cluster. Units are
        thousandths. For example, 12 represents 0.012.
        '''
        return self.data['currentBalance']

    @property
    def currentEVCModeKey(self):
        '''The Enhanced VMotion Compatibility mode that is currently in effect for all hosts
        in this cluster; unset if no EVC mode is active.
        '''
        return self.data['currentEVCModeKey']

    @property
    def currentFailoverLevel(self):
        '''Current failover level. This is the number of physical host failures that can be
        tolerated without impacting the ability to satisfy the minimums for all
        running virtual machines. This represents the current value, as opposed to
        desired value configured by the user.
        '''
        return self.data['currentFailoverLevel']

    @property
    def numVmotions(self):
        '''Total number of migrations with VMotion that have been done internal to this
        cluster.
        '''
        return self.data['numVmotions']

    @property
    def targetBalance(self):
        '''The target balance, in terms of standard deviation, for a DRS cluster. Units are
        thousandths. For example, 12 represents 0.012.
        '''
        return self.data['targetBalance']

