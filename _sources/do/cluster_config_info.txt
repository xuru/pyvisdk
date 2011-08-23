
================================================================================
ClusterConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_compute_resource.ClusterComputeResource`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_das_config_info.ClusterDasConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_das_vm_config_info.ClusterDasVmConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_drs_config_info.ClusterDrsConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_drs_vm_config_info.ClusterDrsVmConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_rule_info.ClusterRuleInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_config_info.ClusterConfigInfo
    
    .. py:attribute:: dasConfig
    
        Cluster-wide configuration of the VMware HA service.
        
    
    .. py:attribute:: dasVmConfig
    
        List of virtual machine configurations for the VMware HA service. Each entry applies to one virtual machine.
        
    
    .. py:attribute:: drsConfig
    
        Cluster-wide configuration of the VMware DRS service.
        
    
    .. py:attribute:: drsVmConfig
    
        List of virtual machine configurations for the VMware DRS service. Each entry applies to one virtual machine.
        
    
    .. py:attribute:: rule
    
        Cluster-wide rules.
        
    