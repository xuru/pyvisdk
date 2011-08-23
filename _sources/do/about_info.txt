
================================================================================
AboutInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_config_summary.HostConfigSummary`,
    :py:class:`~pyvisdk.do.service_content.ServiceContent`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.about_info.AboutInfo
    
    .. py:attribute:: apiType
    
        Indicates whether or not the service instance represents a standalone host. If the service instance represents a standalone host, then the physical inventory for that service instance is fixed to that single host. VirtualCenter server provides additional features over single hosts. For example, VirtualCenter offers multi-host management.
        
    
    .. py:attribute:: apiVersion
    
        The version of the API as a dot-separated string. For example, "1.0.0".
        
    
    .. py:attribute:: build
    
        Build string for the server on which this call is made. For example, x.y.z-num. This string does not apply to the API.
        
    
    .. py:attribute:: fullName
    
        The complete product name, including the version information.
        
    
    .. py:attribute:: instanceUuid
    
        A globally unique identifier associated with this service instance.
        
    
    .. py:attribute:: licenseProductName
    
        The license product name
        
    
    .. py:attribute:: licenseProductVersion
    
        The license product version
        
    
    .. py:attribute:: localeBuild
    
        Build number for the current session's locale. Typically, this is a small number reflecting a localization change from the normal product build.
        
    
    .. py:attribute:: localeVersion
    
        Version of the message catalog for the current session's locale.
        
    
    .. py:attribute:: name
    
        Short form of the product name.
        
    
    .. py:attribute:: osType
    
        Operating system type and architecture.
        
    
    .. py:attribute:: productLineId
    
        The product ID is a unique identifier for a product line.
        
    
    .. py:attribute:: vendor
    
        Name of the vendor of this product.
        
    
    .. py:attribute:: version
    
        Dot-separated version string. For example, "1.2".
        
    