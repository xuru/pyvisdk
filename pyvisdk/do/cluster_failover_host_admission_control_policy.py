
from pyvisdk.do.cluster_das_admission_control_policy import ClusterDasAdmissionControlPolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterFailoverHostAdmissionControlPolicy(ClusterDasAdmissionControlPolicy):
    '''The ClusterFailoverHostAdmissionControlPolicy dedicates one or more hosts for use
        during failover. When a host fails with this policy in place, VMware HA
        attempts to restart its virtual machines on a dedicated failover host. If
        this is not possible, for example the failover host itself has failed or
        it has insufficient resources, HA attempts to restart those virtual
        machines on another host in the cluster.To support the availabilty of a
        failover host, the vCenter Server will prevent users from powering on
        virtual machines on that host, or from using vMotion to migrate virtual
        machines to the host. Also, DRS does not use the failover host for load
        balancing.To obtain the status of a failover host, use the hostStatus
        property (ClusterComputeResourceSummary.admissionControlInfo.hostStatus).
    '''
    
    def __init__(self, failoverHosts):
        # MUST define these
        super(ClusterFailoverHostAdmissionControlPolicy, self).__init__()
    
        self.data['failoverHosts'] = failoverHosts
    
    
    @property
    def failoverHosts(self):
        '''List of references to failover hosts.
        '''
        return self.data['failoverHosts']

