
================================================================================
DistributedVirtualSwitchHostMemberConfigSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dvs_config_spec.DVSConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_host_member_backing.DistributedVirtualSwitchHostMemberBacking`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_keyed_opaque_blob.DistributedVirtualSwitchKeyedOpaqueBlob`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.distributed_virtual_switch_host_member_config_spec.DistributedVirtualSwitchHostMemberConfigSpec
    
    .. py:attribute:: backing
    
        Indicating whether to select individual physical NICs or an existing vSwitch.
        
    
    .. py:attribute:: host
    
        The host to join the DistributedVirtualSwitch in creating a HostMember or identify the existing HostMember to be reconfigured.
        
    
    .. py:attribute:: maxProxySwitchPorts
    
        The maximum number of ports allowed to be created in the proxy switch.
        
    
    .. py:attribute:: operation
    
        The host member operation type. See ConfigSpecOperation for valid values.
        
    
    .. py:attribute:: vendorSpecificConfig
    
        An opaque binary blob that stores vendor specific configuration.
        
    