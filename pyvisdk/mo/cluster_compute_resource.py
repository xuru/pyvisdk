
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.compute_resource import ComputeResource

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterComputeResource(ComputeResource):
    '''The ClusterComputeResource data object aggregates the compute resources of
    associated HostSystem objects into a single compute resource for use by virtual
    machines. The cluster services such as HA (High Availability), DRS (Distributed
    Resource Scheduling), and EVC (Enhanced vMotion Compatibility), enhance the
    utility of this single compute resource.Use the Folder.CreateClusterEx method
    to create an instance of this object.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ClusterComputeResource):
        super(ClusterComputeResource, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def actionHistory(self):
        '''The set of actions that have been performed recently.'''
        return self.update('actionHistory')
    @property
    def configuration(self):
        '''Configuration of the cluster.'''
        return self.update('configuration')
    @property
    def drsFault(self):
        '''A collection of the DRS faults generated in the last DRS invocation. Each
    element of the collection is the set of faults generated in one recommendation.
    DRS faults are generated when DRS tries to make recommendations for rule
    enforcement, power management, etc., and indexed in a tree structure with
    reason for recommendations and VM to migrate (optional) as the index keys.'''
        return self.update('drsFault')
    @property
    def drsRecommendation(self):
        '''If DRS is enabled, this returns the set of recommended migrations from the DRS
    module. The current set of recommendations may be empty, since there may be no
    recommended migrations at this time, or it is possible that DRS is not enabled.'''
        return self.update('drsRecommendation')
    @property
    def migrationHistory(self):
        '''The set of migration decisions that have recently been performed.'''
        return self.update('migrationHistory')
    @property
    def recommendation(self):
        '''List of recommended actions for the cluster. It is possible that the current
    set of recommendations may be empty, either due to not having any running
    dynamic recommendation generation module, or since there may be no recommended
    actions at this time.'''
        return self.update('recommendation')
    
    
    
    def AddHost_Task(self):
        '''Adds a host to the cluster. The hostname must be either an IP address, such as
        192.168.0.1, or a DNS resolvable name. DNS names may be fully qualified names,
        such as host1.domain1.com, or a short name such as host1, providing host1
        resolves to host1.domain1.com. The system uses DNS to resolve short names to
        fully qualified names. If the cluster supports nested resource pools and the
        user specifies the optional ResourcePool argument, then the host's root
        resource pool becomes the specified resource pool. The stand-alone host
        resource hierarchy is imported into the new nested resource pool.If the cluster
        does not support nested resource pools, then the stand-alone host resource
        hierarchy is discarded and all virtual machines on the host are put under the
        cluster's root resource pool.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("AddHost_Task")()
    
    def ApplyRecommendation(self):
        '''Applies a recommendation from the drsRecommendation or the recommendation list.
        Each recommendation can be applied only once.resource.applyRecommendation
        privilege is required if the recommendation is DRS migration or power
        management recommendations.
        :rtype: None
        :returns: 
        '''
        return self.delegate("ApplyRecommendation")()
    
    def CancelRecommendation(self):
        '''Cancels a recommendation. Currently only initial placement recommendations can
        be cancelled. Migration or power management recommendations cannot.
        :rtype: None
        :returns: 
        '''
        return self.delegate("CancelRecommendation")()
    
    def MoveHostInto_Task(self):
        '''Moves an existing host into a cluster. The host must be part of the same
        datacenter, and if the host is part of a cluster, the host must be in
        maintenance mode.If the host is a stand-alone host, the stand-alone
        ComputeResource is removed as part of this operation.All virtual machines
        associated with the host, regardless of whether or not they are running, are
        moved with the host into the cluster. If there are virtual machines that should
        not be moved, then migrate those virtual machines off the host before
        initiating this operation.If the host is a stand-alone host, the cluster
        supports nested resource pools, and the user specifies the optional
        resourcePool argument, then the stand-alone host's root resource pool becomes
        the specified resource pool and the stand-alone host resource hierarchy is
        imported into the new nested resource pool. If the cluster does not support
        nested resource pools or the resourcePool argument is not specified, then the
        stand-alone host resource hierarchy is ignored.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("MoveHostInto_Task")()
    
    def MoveInto_Task(self):
        '''Moves an existing host into a cluster. The host must be part of the same
        datacenter, and if the host is part of a cluster, the host must be in
        maintenance mode.If the host is part of a stand-alone ComputeResource, then the
        stand-alone ComputeResource is removed as part of this operation.All virtual
        machines associated with a host, regardless of whether or not they are running,
        are moved with the host into the cluster. If there are virtual machines that
        should not be moved, then migrate those virtual machines off the host before
        initiating this operation.For stand-alone hosts, the host resource pool
        hierarchy is discarded in this call. To preserve a host resource pools from a
        stand-alone host, call moveHostInt, specifying an optional resource pool. This
        operation is transactional only with respect to each individual host. Hosts in
        the set are moved sequentially and are committed, one at a time. If a failure
        is detected, then the method terminates with an exception. Since hosts are
        moved one at a time, if this operation fails while in the process of moving
        multiple hosts, some hosts are left unmoved.In addition to the privileges
        mentioned, the user must also hold Host.Inventory.EditCluster on the host's
        source ComputeResource object.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("MoveInto_Task")()
    
    def RecommendHostsForVm(self):
        '''Deprecated. As of VI API 2.5, use PowerOnMultiVM_Task. RecommendHostsForVm
        cannot make any recommendations if DRS cannot find the specified host in the
        cluster. With PowerOnMultiVM_Task, DRS attempts to migrate virtual machines and
        power on hosts in standby mode, given the same conditions.Gets a recommendation
        for where to power on, resume, revert from powered-off state to powered on
        state, or to migrate a specific virtual machine. If no host is found, an empty
        list is returned.
        :rtype: 
        :returns: 
        '''
        return self.delegate("RecommendHostsForVm")()
    
    def ReconfigureCluster_Task(self):
        '''Deprecated. As of VI API 2.5, use ReconfigureComputeResource_Task. Reconfigures
        a cluster.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("ReconfigureCluster_Task")()
    
    def RefreshRecommendation(self):
        '''Make DRS invoke again and return a new list of recommendations. Concurrent
        "refresh" requests may be combined together and trigger only one DRS
        invocation.The recommendations generated is stored at recommendation.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RefreshRecommendation")()
    
    def RetrieveDasAdvancedRuntimeInfo(self):
        '''Retrieve DAS advanced runtime info for this cluster.
        :rtype: 
        :returns: 
        '''
        return self.delegate("RetrieveDasAdvancedRuntimeInfo")()