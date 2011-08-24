
================================================================================
HostProxySwitch
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_network_info.HostNetworkInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_proxy_switch_spec.HostProxySwitchSpec`,
    :py:class:`~pyvisdk.do.key_value.KeyValue`,
    :py:class:`~pyvisdk.do.physical_nic.PhysicalNic`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_proxy_switch.HostProxySwitch
    
    .. py:attribute:: dvsName
    
        The name of the DistributedVirtualSwitch that the HostProxySwitch is part of.
        
    
    .. py:attribute:: dvsUuid
    
        The uuid of the DistributedVirtualSwitch that the HostProxySwitch is a part of.
        
    
    .. py:attribute:: key
    
        The proxy switch key.
        
    
    .. py:attribute:: mtu
    
        The maximum transmission unit (MTU) associated with this switch in bytes.
        
    
    .. py:attribute:: numPorts
    
        The number of ports that this switch currently has.
        
    
    .. py:attribute:: numPortsAvailable
    
        The number of ports that are available on this virtual switch.
        
    
    .. py:attribute:: pnic
    
        The set of physical network adapters associated with this switch.
        
    
    .. py:attribute:: spec
    
        The specification of the switch.
        
    
    .. py:attribute:: uplinkPort
    
        The list of ports that can be potentially used by physical nics. This property contains the keys and names of such ports.
        
    