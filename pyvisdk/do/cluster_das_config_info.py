
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasConfigInfo(DynamicData):
    '''The ClusterDasConfigInfo data object contains configuration data about the HA
        service on a cluster.All fields are optional. If you set the parameter to
        when you call ReconfigureComputeResource_Task, an unset property has no
        effect on the existing property value in the cluster configuration on the
        Server. If you set the parameter to when you reconfigure a cluster, the
        cluster configuration is reverted to the default values, then the new
        configuration values are applied.
    '''
    
    def __init__(self, admissionControlEnabled, admissionControlPolicy, defaultVmSettings, enabled, failoverLevel, hostMonitoring, option, vmMonitoring):
        # MUST define these
        super(ClusterDasConfigInfo, self).__init__()
    
        self.data['admissionControlEnabled'] = admissionControlEnabled
        self.data['admissionControlPolicy'] = admissionControlPolicy
        self.data['defaultVmSettings'] = defaultVmSettings
        self.data['enabled'] = enabled
        self.data['failoverLevel'] = failoverLevel
        self.data['hostMonitoring'] = hostMonitoring
        self.data['option'] = option
        self.data['vmMonitoring'] = vmMonitoring
    
    
    @property
    def admissionControlEnabled(self):
        '''Flag that determines whether strict admission control is enabled. When you use
        admission control, the following operations are prevented, if doing so
        would violate the admissionControlPolicy. * Powering on a virtual machine
        in the cluster. * Migrating a virtual machine into the cluster. *
        Increasing the CPU or memory reservation of powered-on virtual machines in
        the cluster.
        '''
        return self.data['admissionControlEnabled']

    @property
    def admissionControlPolicy(self):
        '''Virtual machine admission control policy for VMware HA. The policies specify
        resource availability for failover support. * Host admission policy
        ClusterFailoverHostAdmissionControlPolicy - currently you can specify only
        one failover host. * Failover level policy
        ClusterFailoverLevelAdmissionControlPolicy - the limit of host failures
        for which resources are reserved. When you use the failover level policy,
        HA partitions resources into slots. A slot represents the minimum CPU and
        memory resources that are required to support any powered on virtual
        machine in the cluster. To retrieve information about partitioned
        resources, use the RetrieveDasAdvancedRuntimeInfo method. * Resources
        admission policy ClusterFailoverResourcesAdmissionControlPolicy - CPU and
        memory resources reserved for failover support. When you use the resources
        policy, you can reserve a percentage of the aggregate cluster resource for
        failover.
        '''
        return self.data['admissionControlPolicy']

    @property
    def defaultVmSettings(self):
        '''Cluster-wide defaults for virtual machine HA settings. When a virtual machine has
        no HA configuration (ClusterDasVmConfigSpec), it uses the values specified
        here.
        '''
        return self.data['defaultVmSettings']

    @property
    def enabled(self):
        '''Flag to indicate whether or not VMware HA feature is enabled.
        '''
        return self.data['enabled']

    @property
    def failoverLevel(self):
        '''Configured failover level. This is the number of physical host failures that can
        be tolerated without impacting the ability to satisfy the minimums for all
        running virtual machines. Acceptable values range from one to four.
        '''
        return self.data['failoverLevel']

    @property
    def hostMonitoring(self):
        '''Determines whether HA restarts virtual machines after a host fails. The default
        value is ClusterDasConfigInfoServiceState.enabled. This property is
        meaningful only when ClusterDasConfigInfo.enabled is
        '''
        return self.data['hostMonitoring']

    @property
    def option(self):
        '''Advanced settings.
        '''
        return self.data['option']

    @property
    def vmMonitoring(self):
        '''Level of HA Virtual Machine Health Monitoring service. You can monitor both guest
        and application heartbeats, guest heartbeats only, or you can disable the
        service. The default value is vmMonitoringDisabled.
        '''
        return self.data['vmMonitoring']

