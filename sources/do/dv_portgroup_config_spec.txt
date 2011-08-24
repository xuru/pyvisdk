
================================================================================
DVPortgroupConfigSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.add_dv_portgroup__task.AddDVPortgroup_Task`,
    :py:meth:`~pyvisdk.do.reconfigure_dv_portgroup__task.ReconfigureDVPortgroup_Task`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dv_portgroup_reconfigured_event.DVPortgroupReconfiguredEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_keyed_opaque_blob.DistributedVirtualSwitchKeyedOpaqueBlob`,
    :py:class:`~pyvisdk.do.dv_portgroup_policy.DVPortgroupPolicy`,
    :py:class:`~pyvisdk.do.dv_port_setting.DVPortSetting`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dv_portgroup_config_spec.DVPortgroupConfigSpec
    
    .. py:attribute:: configVersion
    
        The version string of the configuration that this spec is trying to change. This property is required in reconfiguring a portgroup and should be set to the same value as the configVersion. This property is ignored in creating a portgroup if set.
        
    
    .. py:attribute:: defaultPortConfig
    
        The default network setting for all the ports in the portgroup.
        
    
    .. py:attribute:: description
    
        A description string of the portgroup.
        
    
    .. py:attribute:: name
    
        The name of the portgroup.
        
    
    .. py:attribute:: numPorts
    
        Number of ports in the portgroup. Setting this number larger than the number of existing ports in the portgroup causes new ports to be added to the portgroup to meet the number. Setting this property smaller than the number of existing ports deletes the free ports from the portgroup. If the number cannot be met by deleting free ports, a fault is raised. If new ports are added to the portgroup, they are also added to the switch. For portgroups of type ephemeral this property is ignored.
        
    
    .. py:attribute:: policy
    
        Portgroup policy.
        
    
    .. py:attribute:: portNameFormat
    
        The format of the name of the ports when ports are created in the portgroup. For details see portNameFormat.
        
    
    .. py:attribute:: scope
    
        The eligible entities that can connects to the port, for detail see scope.
        
    
    .. py:attribute:: type
    
        The type of portgroup. See DistributedVirtualPortgroupPortgroupType for possible values.
        
    
    .. py:attribute:: vendorSpecificConfig
    
        An opaque binary blob that stores vendor specific configuration.
        
    