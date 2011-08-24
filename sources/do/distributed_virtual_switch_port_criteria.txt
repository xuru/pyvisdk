
================================================================================
DistributedVirtualSwitchPortCriteria
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.fetch_dv_port_keys.FetchDVPortKeys`,
    :py:meth:`~pyvisdk.do.fetch_dv_ports.FetchDVPorts`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.distributed_virtual_switch_port_criteria.DistributedVirtualSwitchPortCriteria
    
    .. py:attribute:: active
    
        If set, only the active ports are qualified.
        
    
    .. py:attribute:: connected
    
        If set, only the connected ports are qualified.
        
    
    .. py:attribute:: inside
    
        If unset, all ports in the switch are qualified. If set to true, only ports inside portgroupKey or any portgroup, if not set, are qualified. If set to false, only ports outside portgroupKey or any portgroup, if not set, are qualified.
        
    
    .. py:attribute:: portgroupKey
    
        The keys of the portgroup that is used for the scope of inside. If this property is unset, it means any portgroup. If inside is unset, this property is ignored.
        
    
    .. py:attribute:: portKey
    
        If set, only the ports of which the key is in the array are qualified.
        
    
    .. py:attribute:: scope
    
        If set, only the ports of which the scope covers the entity are qualified.
        
    
    .. py:attribute:: uplinkPort
    
        If set to true, only the uplink ports are qualified. If set to false, only non-uplink ports are qualified.
        
    