
================================================================================
HostIpRouteEntry
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_ip_route_op.HostIpRouteOp`,
    :py:class:`~pyvisdk.do.host_ip_route_table_info.HostIpRouteTableInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_ip_route_entry.HostIpRouteEntry
    
    .. py:attribute:: deviceName
    
        If available the property indicates the device associated with the routing entry. This property can only be read from the server. It will be ignored if set by the client.
        
    
    .. py:attribute:: gateway
    
        Gateway for the routing entry
        
    
    .. py:attribute:: network
    
        Network of the routing entry Of the format "10.20.120.0" or "2001:db8::1428:57"
        
    
    .. py:attribute:: prefixLength
    
        Prefix length of the network (this is the 22 in 10.20.120.0/22)
        
    