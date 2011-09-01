
================================================================================
HostVirtualSwitchBondBridge
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_virtual_switch_beacon_config.HostVirtualSwitchBeaconConfig`,
    :py:class:`~pyvisdk.do.link_discovery_protocol_config.LinkDiscoveryProtocolConfig`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.host_virtual_switch_bridge.HostVirtualSwitchBridge`
    
.. class:: pyvisdk.do.host_virtual_switch_bond_bridge.HostVirtualSwitchBondBridge
    
    .. py:attribute:: beacon
    
        The beacon configuration to probe for the validity of a link. If this is set, beacon probing is configured and will be used. If this is not set, beacon probing is disabled.
        
    
    .. py:attribute:: linkDiscoveryProtocolConfig
    
        The link discovery protocol configuration for the virtual switch.See LinkDiscoveryProtocolConfig
        
    
    .. py:attribute:: nicDevice
    
        The list of keys of the physical network adapters to be bridged.
        
    