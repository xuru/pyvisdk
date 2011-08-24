
================================================================================
DistributedVirtualSwitchHostMemberPnicSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_host_member_pnic_backing.DistributedVirtualSwitchHostMemberPnicBacking`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.distributed_virtual_switch_host_member_pnic_spec.DistributedVirtualSwitchHostMemberPnicSpec
    
    .. py:attribute:: connectionCookie
    
        The cookie that represents this portConnection instance for the port. The value of this property is generated from the Server. Any value set by an SDK client is ignored.
        
    
    .. py:attribute:: pnicDevice
    
        The physical NIC to be added in the switch. See device.
        
    
    .. py:attribute:: uplinkPortgroupKey
    
        The key of the portgroup to be connected to the physical NIC.
        
    
    .. py:attribute:: uplinkPortKey
    
        The key of the port to be connected to the physical NICs.
        
    