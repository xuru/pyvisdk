
================================================================================
ClusterConfigSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_cluster.CreateCluster`,
    :py:meth:`~pyvisdk.do.reconfigure_cluster__task.ReconfigureCluster_Task`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_das_config_info.ClusterDasConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_das_vm_config_spec.ClusterDasVmConfigSpec`,
    :py:class:`~pyvisdk.do.cluster_drs_config_info.ClusterDrsConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_drs_vm_config_spec.ClusterDrsVmConfigSpec`,
    :py:class:`~pyvisdk.do.cluster_rule_spec.ClusterRuleSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_config_spec.ClusterConfigSpec
    
    .. py:attribute:: dasConfig
    
        Changes to the configuration of VMware HA.
        
    
    .. py:attribute:: dasVmConfigSpec
    
        Changes to the per-virtual-machine VMware HA settings.
        
    
    .. py:attribute:: drsConfig
    
        Changes to the configuration of the VMware DRS service.
        
    
    .. py:attribute:: drsVmConfigSpec
    
        Changes to the per-virtual-machine DRS settings.
        
    
    .. py:attribute:: rulesSpec
    
        Changes to the set of rules.
        
    