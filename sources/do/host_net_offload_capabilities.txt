
================================================================================
HostNetOffloadCapabilities
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_network_policy.HostNetworkPolicy`,
    :py:class:`~pyvisdk.do.host_network_system.HostNetworkSystem`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_net_offload_capabilities.HostNetOffloadCapabilities
    
    .. py:attribute:: csumOffload
    
        (Optional) The flag to indicate whether or not checksum offloading is supported.
        
    
    .. py:attribute:: tcpSegmentation
    
        (Optional) The flag to indicate whether or not TCP segmentation offloading (TSO) is supported.
        
    
    .. py:attribute:: zeroCopyXmit
    
        (Optional) The flag to indicate whether or not zero copy transmits are supported.
        
    