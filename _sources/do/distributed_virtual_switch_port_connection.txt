
================================================================================
DistributedVirtualSwitchPortConnection
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_virtual_nic_connection.HostVirtualNicConnection`,
    :py:class:`~pyvisdk.do.host_virtual_nic_spec.HostVirtualNicSpec`,
    :py:class:`~pyvisdk.do.virtual_ethernet_card_distributed_virtual_port_backing_info.VirtualEthernetCardDistributedVirtualPortBackingInfo`,
    :py:class:`~pyvisdk.do.vnic_port_argument.VnicPortArgument`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.distributed_virtual_switch_port_connection.DistributedVirtualSwitchPortConnection
    
    .. py:attribute:: connectionCookie
    
        The cookie that represents this portConnection instance for the port. The value of this property is generated from the implementation. Any value set in a reconfiguring operation is ignored.
        
    
    .. py:attribute:: portgroupKey
    
        The key of portgroup. If specified, this object represents a connection or an association between a DistributedVirtualPortgroup and a vNIC/pNIC. In this case, setting of portKey is not necessary for a early-binding portgroup and is not allowed for a late-binding portgroup. The portKey property will be populated by the implementation at the time of port binding.
        
    
    .. py:attribute:: portKey
    
        The key of the port. If specified, this object represents a connection or an association between an individual DistributedVirtualPort and a vNIC/pNIC. See portgroupKey for more information on populating this property.
        
    
    .. py:attribute:: switchUuid
    
        The UUID of the switch.
        
    