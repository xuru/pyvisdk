
================================================================================
ClusterDpmHostConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_config_info_ex.ClusterConfigInfoEx`,
    :py:class:`~pyvisdk.do.cluster_dpm_host_config_spec.ClusterDpmHostConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.dpm_behavior.DpmBehavior`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_dpm_host_config_info.ClusterDpmHostConfigInfo
    
    .. py:attribute:: behavior
    
        Specifies the particular DPM behavior for this host.See ClusterDpmConfigInfo
        
    
    .. py:attribute:: enabled
    
        Flag to indicate whether or not VirtualCenter is allowed to perform any power related operations or recommendations for this host. If this flag is false, the host is effectively excluded from DPM service.
        
    
    .. py:attribute:: key
    
        Reference to the host.
        
    