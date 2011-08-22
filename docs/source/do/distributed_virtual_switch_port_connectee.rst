
================================================================================
DistributedVirtualSwitchPortConnectee
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_port.DistributedVirtualPort`,
    :py:class:`~pyvisdk.do.dvs_port_connected_event.DvsPortConnectedEvent`,
    :py:class:`~pyvisdk.do.dvs_port_disconnected_event.DvsPortDisconnectedEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.distributed_virtual_switch_port_connectee.DistributedVirtualSwitchPortConnectee
    
    .. py:attribute:: addressHint
    
        A hint on address information of the NIC that connects to this port.
        
    
    .. py:attribute:: connectedEntity
    
        The connected entity. This property should always be set unless the user's setting does not have System.Read privilege on the object referred to by this property.
        
    
    .. py:attribute:: nicKey
    
        The key of the virtual NIC that connects to this port.
        
    
    .. py:attribute:: type
    
        The type of the connectee. See ConnecteeType for valid values.
        
    