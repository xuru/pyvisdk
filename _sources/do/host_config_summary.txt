
================================================================================
HostConfigSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_list_summary.HostListSummary`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.about_info.AboutInfo`,
    :py:class:`~pyvisdk.do.host_feature_version_info.HostFeatureVersionInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_config_summary.HostConfigSummary
    
    .. py:attribute:: faultToleranceEnabled
    
        The flag to indicate whether or not Fault Tolerance logging is enabled on this host.
        
    
    .. py:attribute:: featureVersion
    
        List of feature-specific version information. Each element refers to the version information for a specific feature.
        
    
    .. py:attribute:: name
    
        The name of the host.
        
    
    .. py:attribute:: port
    
        The port number.
        
    
    .. py:attribute:: product
    
        Information about the software running on the host, if known.
        
    
    .. py:attribute:: sslThumbprint
    
        The SSL thumbprint of the host, if known.
        
    
    .. py:attribute:: vmotionEnabled
    
        The flag to indicate whether or not VMotion is enabled on this host.
        
    