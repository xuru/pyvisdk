
================================================================================
ClusterConfigInfoEx
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_das_config_info.ClusterDasConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_das_vm_config_info.ClusterDasVmConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_dpm_config_info.ClusterDpmConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_dpm_host_config_info.ClusterDpmHostConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_drs_config_info.ClusterDrsConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_drs_vm_config_info.ClusterDrsVmConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_group_info.ClusterGroupInfo`,
    :py:class:`~pyvisdk.do.cluster_rule_info.ClusterRuleInfo`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.compute_resource_config_info.ComputeResourceConfigInfo`
    
.. class:: pyvisdk.do.cluster_config_info_ex.ClusterConfigInfoEx
    
    .. py:attribute:: dasConfig
    
        Cluster-wide configuration of the VMware HA service.
        
    
    .. py:attribute:: dasVmConfig
    
        List of virtual machine configurations for the VMware HA service. Each entry applies to one virtual machine.
        
    
    .. py:attribute:: dpmConfigInfo
    
        Cluster-wide configuration of the VMware DPM service.
        
    
    .. py:attribute:: dpmHostConfig
    
        List of host configurations for the VMware DPM service. Each entry applies to one virtual machine.
        
    
    .. py:attribute:: drsConfig
    
        Cluster-wide configuration of the VMware DRS service.
        
    
    .. py:attribute:: drsVmConfig
    
        List of virtual machine configurations for the VMware DRS service. Each entry applies to one virtual machine.
        
    
    .. py:attribute:: group
    
        Cluster-wide groups.
        
    
    .. py:attribute:: rule
    
        Cluster-wide rules.
        
    