
================================================================================
VAppProductInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.ovf_parse_descriptor_result.OvfParseDescriptorResult`,
    :py:class:`~pyvisdk.do.v_app_product_spec.VAppProductSpec`,
    :py:class:`~pyvisdk.do.virtual_app_summary.VirtualAppSummary`,
    :py:class:`~pyvisdk.do.virtual_machine_config_summary.VirtualMachineConfigSummary`,
    :py:class:`~pyvisdk.do.vm_config_info.VmConfigInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.v_app_product_info.VAppProductInfo
    
    .. py:attribute:: appUrl
    
        URL to entry-point for application. This is often specified using a macro, e.g., http://${app.ip}/, where app.ip is a defined property on the virtual machine or vApp container.
        
    
    .. py:attribute:: classId
    
        class name for this attribute
        
    
    .. py:attribute:: fullVersion
    
        Full-version of the product, e.g., 1.0-build 12323.
        
    
    .. py:attribute:: instanceId
    
        class name for this attribute
        
    
    .. py:attribute:: key
    
        A unqique key for the product section
        
    
    .. py:attribute:: name
    
        Name of the product.
        
    
    .. py:attribute:: productUrl
    
        URL to product homepage.
        
    
    .. py:attribute:: vendor
    
        Vendor of the product.
        
    
    .. py:attribute:: vendorUrl
    
        URL to vendor homepage.
        
    
    .. py:attribute:: version
    
        Short version of the product , e.g., 1.0.
        
    