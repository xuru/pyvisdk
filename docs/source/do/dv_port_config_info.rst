
================================================================================
DVPortConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_port.DistributedVirtualPort`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.dv_port_setting.DVPortSetting`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dv_port_config_info.DVPortConfigInfo
    
    .. py:attribute:: configVersion
    
        The version string of the configuration.
        
    
    .. py:attribute:: description
    
        A description string of the port.
        
    
    .. py:attribute:: name
    
        The name of the port.
        
    
    .. py:attribute:: scope
    
        The eligible entities that can connect to the port. If unset, there is no restriction on which entity can connect to the port. If set, only the entities in the specified list or their child entities are allowed to connect to the port. If scopes are defined at both port and portgroup level, they are taken as an "AND" relationship. If such a relationship doesn't make sense, the reconfigure operation will raise an exception.
        
    
    .. py:attribute:: setting
    
        The network configuration of the port.
        
    