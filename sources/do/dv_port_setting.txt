
================================================================================
DVPortSetting
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dv_port_config_info.DVPortConfigInfo`,
    :py:class:`~pyvisdk.do.dv_port_config_spec.DVPortConfigSpec`,
    :py:class:`~pyvisdk.do.dv_portgroup_config_info.DVPortgroupConfigInfo`,
    :py:class:`~pyvisdk.do.dv_portgroup_config_spec.DVPortgroupConfigSpec`,
    :py:class:`~pyvisdk.do.dvs_config_info.DVSConfigInfo`,
    :py:class:`~pyvisdk.do.dvs_config_spec.DVSConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_policy.BoolPolicy`,
    :py:class:`~pyvisdk.do.dvs_traffic_shaping_policy.DVSTrafficShapingPolicy`,
    :py:class:`~pyvisdk.do.dvs_vendor_specific_config.DVSVendorSpecificConfig`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.v_mware_dvs_port_setting.VMwareDVSPortSetting`
    
.. class:: pyvisdk.do.dv_port_setting.DVPortSetting
    
    .. py:attribute:: blocked
    
        Whether this port is blocked, i.e. packet forwarding is stopped.
        
    
    .. py:attribute:: inShapingPolicy
    
        The network shaping policy for controlling in-throughput.
        
    
    .. py:attribute:: outShapingPolicy
    
        The network shaping policy for controlling out-throughput.
        
    
    .. py:attribute:: vendorSpecificConfig
    
        An opaque binary blob that stores vendor specific configuration.
        
    
    .. py:attribute:: vmDirectPathGen2Allowed
    
        Whether this port is allowed to do VMDirectPath Gen2 network passthrough.
        
    