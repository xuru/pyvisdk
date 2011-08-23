
================================================================================
ClusterDasConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_config_info.ClusterConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_config_info_ex.ClusterConfigInfoEx`,
    :py:class:`~pyvisdk.do.cluster_config_spec.ClusterConfigSpec`,
    :py:class:`~pyvisdk.do.cluster_config_spec_ex.ClusterConfigSpecEx`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_das_admission_control_policy.ClusterDasAdmissionControlPolicy`,
    :py:class:`~pyvisdk.do.cluster_das_vm_settings.ClusterDasVmSettings`,
    :py:class:`~pyvisdk.do.option_value.OptionValue`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_das_config_info.ClusterDasConfigInfo
    
    .. py:attribute:: admissionControlEnabled
    
        Flag that determines whether strict admission control is enabled. When you use admission control, the following operations are prevented, if doing so would violate the admissionControlPolicy. * Powering on a virtual machine in the cluster. * Migrating a virtual machine into the cluster. * Increasing the CPU or memory reservation of powered-on virtual machines in the cluster.
        
    
    .. py:attribute:: admissionControlPolicy
    
        Virtual machine admission control policy for VMware HA. The policies specify resource availability for failover support. * Host admission policy ClusterFailoverHostAdmissionControlPolicy - currently you can specify only one failover host. * Failover level policy ClusterFailoverLevelAdmissionControlPolicy - the limit of host failures for which resources are reserved. When you use the failover level policy, HA partitions resources into slots. A slot represents the minimum CPU and memory resources that are required to support any powered on virtual machine in the cluster. To retrieve information about partitioned resources, use the RetrieveDasAdvancedRuntimeInfo method. * Resources admission policy ClusterFailoverResourcesAdmissionControlPolicy - CPU and memory resources reserved for failover support. When you use the resources policy, you can reserve a percentage of the aggregate cluster resource for failover.
        
    
    .. py:attribute:: defaultVmSettings
    
        Cluster-wide defaults for virtual machine HA settings. When a virtual machine has no HA configuration (ClusterDasVmConfigSpec), it uses the values specified here.
        
    
    .. py:attribute:: enabled
    
        Flag to indicate whether or not VMware HA feature is enabled.
        
    
    .. py:attribute:: failoverLevel
    
        Configured failover level. This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. Acceptable values range from one to four.
        
    
    .. py:attribute:: hostMonitoring
    
        Determines whether HA restarts virtual machines after a host fails. The default value is ClusterDasConfigInfoServiceState.enabled. This property is meaningful only when ClusterDasConfigInfo.enabled is
        
    
    .. py:attribute:: option
    
        Advanced settings.
        
    
    .. py:attribute:: vmMonitoring
    
        Level of HA Virtual Machine Health Monitoring service. You can monitor both guest and application heartbeats, guest heartbeats only, or you can disable the service. The default value is vmMonitoringDisabled.
        
    