
================================================================================
DistributedVirtualSwitchHostMemberConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_host_member.DistributedVirtualSwitchHostMember`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_host_member_backing.DistributedVirtualSwitchHostMemberBacking`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_keyed_opaque_blob.DistributedVirtualSwitchKeyedOpaqueBlob`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.distributed_virtual_switch_host_member_config_info.DistributedVirtualSwitchHostMemberConfigInfo
    
    .. py:attribute:: backing
    
        The backing used by the HostMember.
        
    
    .. py:attribute:: host
    
        The host. This property should always be set unless the user's setting does not have System.Read privilege on the object referred to by this property.
        
    
    .. py:attribute:: maxProxySwitchPorts
    
        The maximum number of ports allowed to be created in the proxy switch.
        
    
    .. py:attribute:: vendorSpecificConfig
    
        An opaque binary blob that stores vendor specific configuration.
        
    