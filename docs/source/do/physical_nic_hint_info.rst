
================================================================================
PhysicalNicHintInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.physical_nic_cdp_info.PhysicalNicCdpInfo`,
    :py:class:`~pyvisdk.do.physical_nic_ip_hint.PhysicalNicIpHint`,
    :py:class:`~pyvisdk.do.physical_nic_name_hint.PhysicalNicNameHint`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_network_hint.QueryNetworkHint`
    
.. class:: pyvisdk.do.physical_nic_hint_info.PhysicalNicHintInfo
    
    .. py:attribute:: connectedSwitchPort
    
        If the uplink is directly connects to a CDP-awared network device and the device's CDP broadcast is enabled, this property will be set to return the CDP information that vmkernel received on this PNIC. CDP data contains the device information and port ID that the PNIC connects to. If the uplink is not connecting to a CDP-awared device or CDP is not enabled on the device, this property will be unset. PhysicalNicCdpInfo
        
    
    .. py:attribute:: device
    
        The physical network adapter device to which this hint applies.
        
    
    .. py:attribute:: network
    
        The list of network names that were detected on this physical network adapter.
        
    
    .. py:attribute:: subnet
    
        The list of subnets that were detected on this physical network adapter.
        
    