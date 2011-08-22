
================================================================================
ClusterConfigSpecEx
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_cluster_ex.CreateClusterEx`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_das_config_info.ClusterDasConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_das_vm_config_spec.ClusterDasVmConfigSpec`,
    :py:class:`~pyvisdk.do.cluster_dpm_config_info.ClusterDpmConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_dpm_host_config_spec.ClusterDpmHostConfigSpec`,
    :py:class:`~pyvisdk.do.cluster_drs_config_info.ClusterDrsConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_drs_vm_config_spec.ClusterDrsVmConfigSpec`,
    :py:class:`~pyvisdk.do.cluster_group_spec.ClusterGroupSpec`,
    :py:class:`~pyvisdk.do.cluster_rule_spec.ClusterRuleSpec`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.compute_resource_config_spec.ComputeResourceConfigSpec`
    
.. class:: pyvisdk.do.cluster_config_spec_ex.ClusterConfigSpecEx
    
    .. py:attribute:: dasConfig
    
        HA configuration; includes default settings for virtual machines.
        
    
    .. py:attribute:: dasVmConfigSpec
    
        HA configuration for individual virtual machines. The entries in this array override the cluster default settings (ClusterDasConfigInfo.defaultVmSettings). You cannot specify an HA override for a secondary FT virtual machine. The secondary virtual machine will inherit whatever settings apply to its primary virtual machine. If you include an entry for a secondary, the reconfigure method will throw the fault CannotChangeHaSettingsForFtSecondary.
        
    
    .. py:attribute:: dpmConfig
    
        DPM configuration; includes default settings for hosts.
        
    
    .. py:attribute:: dpmHostConfigSpec
    
        DPM configuration for individual hosts. The entries in this array override the cluster default settings (ClusterDpmConfigInfo.defaultDpmBehavior).
        
    
    .. py:attribute:: drsConfig
    
        DRS configuration; includes default settings for virtual machines.
        
    
    .. py:attribute:: drsVmConfigSpec
    
        DRS configuration for individual virtual machines. The entries in this array override the cluster default settings (ClusterDrsConfigInfo.defaultVmBehavior). You cannot specify a DRS override for a secondary FT virtual machine. The secondary virtual machine will inherit whatever setting applies to its primary virtual machine. If you include an entry for a secondary, the reconfigure method will throw the fault CannotChangeDrsBehaviorForFtSecondary.
        
    
    .. py:attribute:: groupSpec
    
        Cluster-wide group configuration. The array contains one or more group specification objects. A group specification object contains a virtual machine group (ClusterVmGroup) or a host group (ClusterHostGroup). Groups can be related; see ClusterVmHostRuleInfo.
        
    
    .. py:attribute:: rulesSpec
    
        Cluster affinity and anti-affinity rule configuration.
        
    