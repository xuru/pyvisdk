
================================================================================
VMwareDVSPvlanMapEntry
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.v_mware_dvs_config_info.VMwareDVSConfigInfo`,
    :py:class:`~pyvisdk.do.v_mware_dvs_pvlan_config_spec.VMwareDVSPvlanConfigSpec`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.v_mware_dvs_pvlan_map_entry.VMwareDVSPvlanMapEntry
    
    .. py:attribute:: primaryVlanId
    
        The primary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.
        
    
    .. py:attribute:: pvlanType
    
        The type of PVLAN. See VmwareDistributedVirtualSwitchPvlanPortType for valid values.
        
    
    .. py:attribute:: secondaryVlanId
    
        The secondary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.
        
    