
================================================================================
DistributedVirtualPort
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_port_connectee.DistributedVirtualSwitchPortConnectee`,
    :py:class:`~pyvisdk.do.dv_port_config_info.DVPortConfigInfo`,
    :py:class:`~pyvisdk.do.dv_port_state.DVPortState`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.fetch_dv_ports.FetchDVPorts`
    
.. class:: pyvisdk.do.distributed_virtual_port.DistributedVirtualPort
    
    .. py:attribute:: config
    
        The management configuration of the port.
        
    
    .. py:attribute:: conflict
    
        Whether the port is a conflict port. A port could be marked as conflict if an entity is discovered connecting to a port that is already occupied, or if the port is created by the host without conferring with vCenter Server. A conflict port will not have its runtime state persisted and the port can't move away from the host, that is, no VMotion if a Virtual Machine is using a conflict port.
        
    
    .. py:attribute:: conflictPortKey
    
        If the port is marked conflict in the case of two entities connecting to the same port (see conflict), this is the key of the port which the connected entity is contending for.
        
    
    .. py:attribute:: connectee
    
        The entity that connects to the port.
        
    
    .. py:attribute:: connectionCookie
    
        This is a cookie representing the current instance of association between port and vNIC/pNIC (which is represented as DistributedVirtualSwitchPortConnection objects). The same cookie is present on the pNIC/vNIC configuration (see connectionCookie) in order for the port to authenticate that the peer is the rightful connectee of the port.
        
    
    .. py:attribute:: dvsUuid
    
        The UUID of DistributedVirtualSwitch that the port belongs to.
        
    
    .. py:attribute:: key
    
        The port key.
        
    
    .. py:attribute:: lastStatusChange
    
        The last time the runtimeInfo value was changed.
        
    
    .. py:attribute:: portgroupKey
    
        The key of the portgroup that the port belongs to, if any.
        
    
    .. py:attribute:: proxyHost
    
        The host that services this port
        
    
    .. py:attribute:: state
    
        The runtime state of the port.
        
    