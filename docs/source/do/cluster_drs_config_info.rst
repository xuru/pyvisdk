
================================================================================
ClusterDrsConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_config_info.ClusterConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_config_info_ex.ClusterConfigInfoEx`,
    :py:class:`~pyvisdk.do.cluster_config_spec.ClusterConfigSpec`,
    :py:class:`~pyvisdk.do.cluster_config_spec_ex.ClusterConfigSpecEx`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.drs_behavior.DrsBehavior`,
    :py:class:`~pyvisdk.do.option_value.OptionValue`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_drs_config_info.ClusterDrsConfigInfo
    
    .. py:attribute:: defaultVmBehavior
    
        Specifies the cluster-wide default DRS behavior for virtual machines. You can override the default behavior for a virtual machine by using the ClusterDrsVmConfigInfo object.
        
    
    .. py:attribute:: enabled
    
        Flag indicating whether or not the service is enabled.
        
    
    .. py:attribute:: enableVmBehaviorOverrides
    
        Flag that dictates whether DRS Behavior overrides for individual virtual machines (ClusterDrsVmConfigInfo) are enabled. The default value is
        
    
    .. py:attribute:: option
    
        Advanced settings.
        
    
    .. py:attribute:: vmotionRate
    
        Threshold for generated ClusterRecommendations. DRS generates only those recommendations that are above the specified vmotionRate. Ratings vary from 1 to 5. This setting applies to manual, partiallyAutomated, and fullyAutomated DRS clusters. See DrsBehavior.
        
    