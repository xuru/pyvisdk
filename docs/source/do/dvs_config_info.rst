
================================================================================
DVSConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch.DistributedVirtualSwitch`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_portgroup.DistributedVirtualPortgroup`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_host_member.DistributedVirtualSwitchHostMember`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_keyed_opaque_blob.DistributedVirtualSwitchKeyedOpaqueBlob`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_product_spec.DistributedVirtualSwitchProductSpec`,
    :py:class:`~pyvisdk.do.dv_port_setting.DVPortSetting`,
    :py:class:`~pyvisdk.do.dvs_contact_info.DVSContactInfo`,
    :py:class:`~pyvisdk.do.dvs_policy.DVSPolicy`,
    :py:class:`~pyvisdk.do.dvs_uplink_port_policy.DVSUplinkPortPolicy`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.v_mware_dvs_config_info.VMwareDVSConfigInfo`
    
.. class:: pyvisdk.do.dvs_config_info.DVSConfigInfo
    
    .. py:attribute:: configVersion
    
        The version string of the configuration.
        
    
    .. py:attribute:: contact
    
        The human operator contact information.
        
    
    .. py:attribute:: createTime
    
        The create time of the switch.
        
    
    .. py:attribute:: defaultPortConfig
    
        The default configuration for the ports in the switch, if the port does not inherit configuration from the parent portgroup or has its own configuration.
        
    
    .. py:attribute:: description
    
        A description string of the switch.
        
    
    .. py:attribute:: extensionKey
    
        The key of the extension registered by the remote server that controls the switch.
        
    
    .. py:attribute:: host
    
        The hosts that join the switch.
        
    
    .. py:attribute:: maxPorts
    
        The maximum number of ports allowed in the switch, not including conflict ports.
        
    
    .. py:attribute:: name
    
        The name of the switch.
        
    
    .. py:attribute:: networkResourceManagementEnabled
    
        Boolean to indicate if network I/O control is enabled on the switch.
        
    
    .. py:attribute:: numPorts
    
        Current number of ports, not including conflict ports.
        
    
    .. py:attribute:: numStandalonePorts
    
        The number of standalone ports in the switch. Standalone ports are ports that do not belong to any portgroup.
        
    
    .. py:attribute:: policy
    
        The usage policy of the switch.
        
    
    .. py:attribute:: productInfo
    
        The vendor, product, and version information for the implementation module of the switch.
        
    
    .. py:attribute:: targetInfo
    
        The intended vendor, product, and version information for the implementation module of the switch.
        
    
    .. py:attribute:: uplinkPortgroup
    
        The uplink portgroups. When adding host members, a number of uplink ports, based on uplinkPortPolicy, are created for the host. If portgroups are shown here, those uplink ports will be added to the portgroups, with uplink ports evenly spread among the portgroups.
        
    
    .. py:attribute:: uplinkPortPolicy
    
        The uplink port policy.
        
    
    .. py:attribute:: uuid
    
        The generated UUID of the switch. Unique across vCenter Server inventory and instances.
        
    
    .. py:attribute:: vendorSpecificConfig
    
        An opaque binary blob that stores vendor specific configuration.
        
    