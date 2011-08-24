
================================================================================
DVSConfigSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dvs_create_spec.DVSCreateSpec`,
    :py:class:`~pyvisdk.do.dvs_reconfigured_event.DvsReconfiguredEvent`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.v_mware_dvs_config_spec.VMwareDVSConfigSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.reconfigure_dvs__task.ReconfigureDvs_Task`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_portgroup.DistributedVirtualPortgroup`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_host_member_config_spec.DistributedVirtualSwitchHostMemberConfigSpec`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_keyed_opaque_blob.DistributedVirtualSwitchKeyedOpaqueBlob`,
    :py:class:`~pyvisdk.do.dv_port_setting.DVPortSetting`,
    :py:class:`~pyvisdk.do.dvs_contact_info.DVSContactInfo`,
    :py:class:`~pyvisdk.do.dvs_policy.DVSPolicy`,
    :py:class:`~pyvisdk.do.dvs_uplink_port_policy.DVSUplinkPortPolicy`
    
.. class:: pyvisdk.do.dvs_config_spec.DVSConfigSpec
    
    .. py:attribute:: configVersion
    
        The version string of the configuration that this spec is trying to change. This property is required in reconfiguring a switch and should be set to the same value as configVersion. This property is ignored during switch creation.
        
    
    .. py:attribute:: contact
    
        Set the human operator contact information.
        
    
    .. py:attribute:: defaultPortConfig
    
        The default configuration for ports.
        
    
    .. py:attribute:: description
    
        Set the description string of the switch.
        
    
    .. py:attribute:: extensionKey
    
        The key of the extension registered by a remote server that controls the switch.
        
    
    .. py:attribute:: host
    
        The host member specification. A host should have only one entry in this array. Duplicate entries for the same host will raise a fault.
        
    
    .. py:attribute:: maxPorts
    
        The maximum number of DistributedVirtualPorts allowed in the switch. If specified in a reconfigure operation, this number cannot be smaller than the number of existing DistributedVirtualPorts.
        
    
    .. py:attribute:: name
    
        The name of the switch. Must be unique in the parent folder.
        
    
    .. py:attribute:: numStandalonePorts
    
        The number of standalone ports in the switch. Standalone ports are ports that do not belong to any portgroup. If set to a number larger than number of existing standalone ports in the switch, new ports get created to meet the number. If set to a number smaller than the number of existing standalone ports, free ports (uplink ports excluded) are deleted to meet the number. If the set number cannot be met by deleting free standalone ports, a fault is raised.
        
    
    .. py:attribute:: policy
    
        The usage policy of the switch.
        
    
    .. py:attribute:: uplinkPortgroup
    
        The uplink portgroups.
        
    
    .. py:attribute:: uplinkPortPolicy
    
        The uplink port policy.
        
    
    .. py:attribute:: vendorSpecificConfig
    
        Set the opaque blob that stores vendor specific configuration.
        
    