
================================================================================
DVPortgroupConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_portgroup.DistributedVirtualPortgroup`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch.DistributedVirtualSwitch`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_keyed_opaque_blob.DistributedVirtualSwitchKeyedOpaqueBlob`,
    :py:class:`~pyvisdk.do.dv_portgroup_policy.DVPortgroupPolicy`,
    :py:class:`~pyvisdk.do.dv_port_setting.DVPortSetting`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dv_portgroup_config_info.DVPortgroupConfigInfo
    
    .. py:attribute:: configVersion
    
        The version string of the configuration.
        
    
    .. py:attribute:: defaultPortConfig
    
        The common network setting for all the ports in the portgroup.
        
    
    .. py:attribute:: description
    
        A description string of the portgroup.
        
    
    .. py:attribute:: distributedVirtualSwitch
    
        The DistributedVirtualSwitch that the portgroup is defined on. This property should always be set unless the user's setting does not have System.Read privilege on the object referred to by this property.
        
    
    .. py:attribute:: key
    
        The key of the portgroup.
        
    
    .. py:attribute:: name
    
        The name of the portgroup.
        
    
    .. py:attribute:: numPorts
    
        Number of ports in the portgroup.
        
    
    .. py:attribute:: policy
    
        Portgroup policy.
        
    
    .. py:attribute:: portNameFormat
    
        If set, a name will be automatically generated based on this format string for a port when it is created in or moved into the portgroup. The format string can contain meta tags that will be resolved to the corresponding values in generating a name, if applicable for the port at the time of name generation.
        
    
    .. py:attribute:: scope
    
        The eligible entities that can connect to the portgroup. If unset, there is no restriction on which entity can connect to the portgroup. If set, only the entities in the specified list or their child entities are allowed to connect to the portgroup. If scopes are defined at both port and portgroup level, they are taken as an "AND" relationship. If such a relationship doesn't make sense, the reconfigure operation will raise an exception.
        
    
    .. py:attribute:: type
    
        The type of portgroup. See DistributedVirtualPortgroupPortgroupType for possible values.
        
    
    .. py:attribute:: vendorSpecificConfig
    
        An opaque binary blob that stores vendor specific configuration.
        
    