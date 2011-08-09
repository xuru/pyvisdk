
from pyvisdk.do.cluster_das_host_info import ClusterDasHostInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasAamHostInfo(ClusterDasHostInfo):
    '''The ClusterDasAamHostInfo object contains a list of the ESX hosts in an HA cluster
        and a list that identifies the hosts. (AAM is a component of the HA
        service.) The primary hosts share the joint responsibility of maintaining
        all cluster state and one will initiate failover actions should a failure
        occur.When you add an ESX host to a VMware HA cluster, the host downloads
        HA agent components from the vCenter Server. The HA agent maintains
        communication with the vCenter Server.When the host downloads the HA
        agent, the host configures the agent to communicate with other agents in
        the cluster. A host that joins the cluster communicates with an existing
        primary host to complete its configuration (except when you are adding the
        first host to the cluster).* The first five hosts added to the cluster are
        designated as primary hosts. All subsequent hosts are designated as
        secondary hosts. * If a primary host is removed from the cluster, the
        vCenter Server promotes another host to primary status. * There must be at
        least one functional primary host for VMware HA to operate correctly. If
        there is not an available primary host (no response), host configuration
        for HA will fail. If there is a total cluster failure, HA will begin
        restarting virtual machines as soon as one host recovers and its HA agent
        is up and running.One of the primary hosts assumes the role of the active
        primary host. The active primary host responsibilities include the
        following activities:* Decides where to restart virtual machines. * Tracks
        failed restart attempts. * Determines when it is appropriate to continue
        attempts to restart a virtual machine.If the active primary host fails,
        another primary host replaces it.
    '''
    
    def __init__(self, hostDasState, primaryHosts):
        # MUST define these
        super(ClusterDasAamHostInfo, self).__init__()
    
        self.data['hostDasState'] = hostDasState
        self.data['primaryHosts'] = primaryHosts
    
    
    @property
    def hostDasState(self):
        '''The state of HA on the hosts.
        '''
        return self.data['hostDasState']

    @property
    def primaryHosts(self):
        '''The list of primary hosts.
        '''
        return self.data['primaryHosts']

