
================================================================================
DVPortgroupPolicy
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dv_portgroup_config_info.DVPortgroupConfigInfo`,
    :py:class:`~pyvisdk.do.dv_portgroup_config_spec.DVPortgroupConfigSpec`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.v_mware_dvs_portgroup_policy.VMwareDVSPortgroupPolicy`
    
.. class:: pyvisdk.do.dv_portgroup_policy.DVPortgroupPolicy
    
    .. py:attribute:: blockOverrideAllowed
    
        Allow the blocked setting of an individual port to override the setting in defaultPortConfig of a portgroup.
        
    
    .. py:attribute:: livePortMovingAllowed
    
        Allow a live port to be moved in and out of the portgroup.
        
    
    .. py:attribute:: portConfigResetAtDisconnect
    
        If true, reset the port network setting back to the portgroup setting (thus removing the per-port setting) when the port is disconnected from the connectee.
        
    
    .. py:attribute:: shapingOverrideAllowed
    
        Allow the inShapingPolicy or outShapingPolicy settings of an individual port to override the setting in defaultPortConfig of a portgroup.
        
    
    .. py:attribute:: vendorConfigOverrideAllowed
    
        Allow the vendorSpecificConfig setting of an individual port to override the setting in defaultPortConfig of a portgroup.
        
    