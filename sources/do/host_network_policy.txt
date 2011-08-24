
================================================================================
HostNetworkPolicy
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_port_group.HostPortGroup`,
    :py:class:`~pyvisdk.do.host_port_group_spec.HostPortGroupSpec`,
    :py:class:`~pyvisdk.do.host_virtual_switch_spec.HostVirtualSwitchSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_net_offload_capabilities.HostNetOffloadCapabilities`,
    :py:class:`~pyvisdk.do.host_network_security_policy.HostNetworkSecurityPolicy`,
    :py:class:`~pyvisdk.do.host_network_traffic_shaping_policy.HostNetworkTrafficShapingPolicy`,
    :py:class:`~pyvisdk.do.host_nic_teaming_policy.HostNicTeamingPolicy`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_network_policy.HostNetworkPolicy
    
    .. py:attribute:: nicTeaming
    
        The network adapter teaming policy. The bridge must be BondBridge for this property to be valid.
        
    
    .. py:attribute:: offloadPolicy
    
        Offload capabilities are used to optimize virtual machine network performance. When a virtual machine is transmitting on a network, some operations can be offloaded to either the host or the physical hardware. This policy indicates what networking related operations should be offloaded.
        
    
    .. py:attribute:: security
    
        The security policy governing ports on this virtual switch.
        
    
    .. py:attribute:: shapingPolicy
    
        The traffic shaping policy.
        
    