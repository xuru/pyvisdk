
================================================================================
PhysicalNicCdpDeviceCapability
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.physical_nic_cdp_info.PhysicalNicCdpInfo`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.physical_nic_cdp_device_capability.PhysicalNicCdpDeviceCapability
    
    .. py:attribute:: host
    
        The CDP-awared device has the capability of a host, which Sends and receives packets for at least one network layer protocol.
        
    
    .. py:attribute:: igmpEnabled
    
        The CDP-awared device is IGMP-enabled, which does not forward IGMP Report packets on nonrouter ports.
        
    
    .. py:attribute:: networkSwitch
    
        The CDP-awared device has the capability of switching. The difference between this capability and transparentBridge is that a switch does not run the Spanning-Tree Protocol. This device is assumed to be deployed in a physical loop-free topology.
        
    
    .. py:attribute:: repeater
    
        The CDP-awared device has the capability of a repeater
        
    
    .. py:attribute:: router
    
        The CDP-awared device has the capability of a routing for at least one network layer protocol
        
    
    .. py:attribute:: sourceRouteBridge
    
        The CDP-awared device has the capability of source-route bridging
        
    
    .. py:attribute:: transparentBridge
    
        The CDP-awared device has the capability of transparent bridging
        
    