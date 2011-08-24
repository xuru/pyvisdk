
================================================================================
ClusterDpmConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_config_info_ex.ClusterConfigInfoEx`,
    :py:class:`~pyvisdk.do.cluster_config_spec_ex.ClusterConfigSpecEx`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.dpm_behavior.DpmBehavior`,
    :py:class:`~pyvisdk.do.option_value.OptionValue`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_dpm_config_info.ClusterDpmConfigInfo
    
    .. py:attribute:: defaultDpmBehavior
    
        Specifies the default VMware DPM behavior for hosts. This default behavior can be overridden on a per host basis using the ClusterDpmHostConfigInfo object.
        
    
    .. py:attribute:: enabled
    
        Flag indicating whether or not the service is enabled. This service can not be enabled, unless DRS is enabled as well.
        
    
    .. py:attribute:: hostPowerActionRate
    
        DPM generates only those recommendations that are above the specified rating. Ratings vary from 1 to 5. This setting applies to both manual and automated (@link DpmBehavior) DPM clusters.
        
    
    .. py:attribute:: option
    
        Advanced settings.
        
    